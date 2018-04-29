import gensim
from gensim import corpora, models
import pyLDAvis.gensim

import nltk
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string # allows us to define punctutation to remove
from nltk.corpus import wordnet as wn # allows us to access pos types

from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
from pandas import DataFrame, Series
import numpy as np


wordnet_lemmatizer = WordNetLemmatizer()

# change words to lowercase in a list
def convertToLowercase(text):
    return [word.lower() for word in text]

# remove punctuation from the string
def removePunctuation(text):
    exclude = set(string.punctuation)
    keep_these_punct = []
    for punct in keep_these_punct:
        exclude.remove(punct)
    converted_text = ''.join(ch for ch in text if ch not in exclude)
    return converted_text





def get_stopset(extra_stopwords):
    stopset = set(nltk.corpus.stopwords.words('english'))
    for word in extra_stopwords:
        stopset.add(word)
    return stopset

# removes stop words from a list of words
def removeStopWords(text, added_words):
    stopset = get_stopset(added_words)
    return [word for word in text if word not in stopset]

# checks if a word isnt in the stopset
def notStopWord(word, added_words):
    stopset = get_stopset(added_words)
    return word not in stopset



# Apply lemmatization to words in a list
def lemmatizeWords(words):
    convert_words = []
    words_with_pos = nltk.pos_tag(words)
    for pos_tag in words_with_pos:
        simplify_pos = penn_to_wn(pos_tag[1])
        if(simplify_pos == None):
            convert_words.append(wordnet_lemmatizer.lemmatize(pos_tag[0]))
        else:
            convert_words.append(wordnet_lemmatizer.lemmatize(pos_tag[0], simplify_pos))
    #print(words == convert_words)
    return convert_words


# Apply part of speech tagging to a list of words
def partOfSpeechTag(words):
    return nltk.pos_tag(words)

## the following functions check what a tag is
def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None



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

    top_20_words = pd.DataFrame(columns = top_20_columns)

    for person in top_20_per_candidate:
        words = [x for x,y in top_20_per_candidate[person]]
        values = [person] + words
        one_row = pd.DataFrame(columns = top_20_columns)
        one_row.loc[0] = values
        frames = [top_20_words, one_row]
        top_20_words = pd.concat(frames)

    with open(output_file, 'w') as f:
        f.write(top_20_words.to_json(orient = "records"))

    ids_for_words_cols = ["candidate_id", "word_ranking", "value"]
    ids_for_words = pd.DataFrame(columns = ids_for_words_cols)

    for person in top_20_per_candidate:
        values = [y for x,y in top_20_per_candidate[person]]
        for i in range(0,len(values)):
            row_values = [person, i+1, values[i]]
            one_row = pd.DataFrame(columns = ids_for_words_cols)
            one_row.loc[0] = row_values
            frames = [ids_for_words, one_row]
            ids_for_words = pd.concat(frames)

    with open(output_file_values, 'w') as f:
        f.write(ids_for_words.to_json(orient = "records"))


def create_lda_page(final_corpus, page_name):
    #start_time = time.time()

    dictionary = corpora.Dictionary(final_corpus)

    # Converts dictionary into a bag-of-words.
    corpusVec = [dictionary.doc2bow(text) for text in final_corpus]

    # Generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpusVec, num_topics=10, id2word = dictionary, passes=500)
    # print(ldamodel.print_topics(num_topics=5, num_words=5))

    vis_data = pyLDAvis.gensim.prepare(ldamodel, corpusVec, dictionary)

    pyLDAvis.save_html(vis_data, page_name)
    #print("--- %s seconds ---" % (time.time() - start_time))
