import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nlp_functions import*
from clean_data import return_data

def get_relevant_sentences(sentences, candidate_id, candidate_table):
    name = return_data(candidate_table, "id", candidate_id, "name")
    relevant = []
    for sentence in sentences:
        sentence = sentence.lower()
        name = name.lower()
        if (name in sentence) or (name.split()[-1] in sentence):
            relevant.append(sentence)

    return relevant

def candidate_in_sentence(sentence, candidate_id, candidate_table):
    name = return_data(candidate_table, "id", candidate_id, "name").lower()
    sentence = sentence.lower()
    return ((name in sentence) or (name.split()[-1] in sentence))


def get_sentiment(input_file, output_file, candidate_table):
    article = pd.read_json(input_file)
    sent_data = {}
    analyzer = SentimentIntensityAnalyzer()
    for index,row in article.iterrows():
        text = row["article_text"]
        sentences = sent_tokenize(text)
        #sentences = get_relevant_sentences(sentences, row['candidate_fk'], candidate)
        summed = {'neg':0.0, "neu":0.0, "pos":0.0, "num_sentences":0}
        for sentence in sentences:
            vs = analyzer.polarity_scores(sentence)
            #sentiment = TextBlob(sentence)
            #print(sentiment.sentiment)
            weight = 1
            if(candidate_in_sentence(sentence, row['candidate_fk'], candidate_table)):
                weight = 10
            if vs['neg'] > vs['pos']:
                summed['neg'] += weight*1
            elif vs['pos'] > vs['neg']:
                summed['pos'] += weight*1
            summed['num_sentences'] += 1
            sent_data[index] = summed
            #print(index, len(sentences),summed)
        summed = sent_data[index]['neg'] + sent_data[index]['pos']
        #print(summed)
        if summed != 0:
            difference =  (sent_data[index]['pos'] - sent_data[index]['neg'])/summed
        else:
            difference = 1

        percentage = ((difference+1)/2)*100
        article.at[index,"sentiment_score"] = int(percentage)

    with open(output_file, 'w') as f:
        f.write(article.to_json(orient = "records"))
