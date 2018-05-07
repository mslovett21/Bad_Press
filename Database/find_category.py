from nlp_functions import*
from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
from pandas import DataFrame, Series
import numpy as np

import math

from clean_data import return_data



def find_categories_and_top_20(words_to_remove, candidate_info, input_file, output_file, output_file_values):

    all_data = pd.read_json(input_file)

    corpus_text = []
    for index,row in all_data.iterrows():
        corpus_text.append(row['article_text'])

    corpus_sentences = [sent_tokenize(x) for x in corpus_text]
    corpus_words = []
    for x in corpus_sentences:
        corpus_words.append(([lemmatizeWords(convertToLowercase(removePunctuation(y).split())) for y in x]))
    #corpus_words = [removeStopWords(WhitespaceTokenizer().tokenize(x)) for x in corpus]

    final_corpus = []
    for x in corpus_words:
        final_corpus.append([item for sublist in x for item in removeStopWords(sublist, words_to_remove) if item.isalpha()])

    relevant_words_text_string = [" ".join(y) for y in final_corpus]


    # create dictionary: map candidate to list of articles they appear in
    articles_per_candidate = {}

    for i in range(len(all_data)):
        candidate_id = all_data["candidate_fk"][i]
        if candidate_id in articles_per_candidate:
            articles_per_candidate[candidate_id].append(i)
        else:
            articles_per_candidate[candidate_id] = [i]


    tf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 0, stop_words = 'english')

    tfidf_matrix =  tf.fit_transform(relevant_words_text_string)
    feature_names = tf.get_feature_names()

    dense = tfidf_matrix.todense()


    top_20_per_candidate = {}

    for person in articles_per_candidate:
        candidate_articles = articles_per_candidate[person]
        summed_values = [0]*len(feature_names)

        phrase_scores = []
        sorted_scores = []
        word_val_pair = []
        for article_id in candidate_articles:
            article_vector = dense[article_id].tolist()[0]
            summed_values = [x+y for x,y in zip(summed_values,article_vector)]

        pairs = list(zip(range(0, len(feature_names)), summed_values))

        phrase_scores = [pair for pair in pairs if pair[1] > 0]

        sorted_scores = sorted(phrase_scores, key=lambda x: x[1], reverse=True)[0:20]

        word_val_pair = []
        for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_scores][:]:
            word_val_pair.append((phrase,score))

        top_20_per_candidate[person] = word_val_pair

    top_20_columns = ["id"]
    top_20_columns.extend(["word_"+str(x) for x in range(1,21)])
    top_20_columns.append("last_name")

    top_20_words = pd.DataFrame(columns = top_20_columns)

    for person in top_20_per_candidate:
        full_name = return_data(candidate_info, "id", person, "name").split()
        last_name = full_name[-1]
        words = [x for x,y in top_20_per_candidate[person]]
        values = [person] + words + [last_name]
        one_row = pd.DataFrame(columns = top_20_columns)
        one_row.loc[0] = values
        frames = [top_20_words, one_row]
        top_20_words = pd.concat(frames)

    with open(output_file, 'w') as f:
        f.write(top_20_words.to_json(orient = "records"))

    ids_for_words_cols = ["candidate_id", "word_ranking", "value", "last_name"]
    ids_for_words = pd.DataFrame(columns = ids_for_words_cols)

    for person in top_20_per_candidate:
        values = [y for x,y in top_20_per_candidate[person]]
        full_name = return_data(candidate_info, "id", person, "name").split()
        last_name = full_name[-1]
        for i in range(0,len(values)):
            row_values = [person, i+1, math.floor(10*values[i]), last_name]
            one_row = pd.DataFrame(columns = ids_for_words_cols)
            one_row.loc[0] = row_values
            frames = [ids_for_words, one_row]
            ids_for_words = pd.concat(frames)

    with open(output_file_values, 'w') as f:
        f.write(ids_for_words.to_json(orient = "records"))
