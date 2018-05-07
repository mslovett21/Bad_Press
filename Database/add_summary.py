import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def get_summary(text, threshold):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    #for wordValue, freq in freqTable.items():
    #    print(wordValue, freq)
    sentences = sent_tokenize(text)
    #print(sentences)
    sentenceValue = dict()

    for sentence in sentences:
        for word, value in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    #print(sentence, wordValue)
                    #print(wordValue[1])
                    sentenceValue[sentence] += value
                else:
                    sentenceValue[sentence] = value

    for k,v in sentenceValue.copy().items():
        sentenceValue[k] = sentenceValue[k]/len(word_tokenize(sentence))

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from original text
    average = int(sumValues/ len(sentenceValue))

    summary = ''
    #print(len(sentences))
    for sentence in sentences:
        if sentence in sentenceValue and sentenceValue[sentence] >= (threshold * average):
            summary +=  " " + sentence
    #print("final",len(summary) )
    return summary

def find_empty_summary(no_summary, threshold, all_data):
    #print("input ", no_summary, threshold)
    empty_summary = []
    for i in no_summary:
        try:
            text_summary = get_summary(all_data.at[i, "article_text"],threshold)
            all_data.at[i, 'summary'] = text_summary
            if len(text_summary) == 0:
                empty_summary.append(i)
        except KeyError:
            #print("not there")
            empty_summary.append(i)
    #print("output", empty_summary)
    return empty_summary

def get_some_summary(all_data):
    current_threshold = 1.4
    no_summary = [i for i in range(size) if all_data.at[i,'summary'] == '']
    while(no_summary != [] and current_threshold >= 1.0):
        no_summary = find_empty_summary(no_summary, current_threshold, all_data)
        current_threshold = round(current_threshold - .1, 2)

    return all_data

def add_summary(input_file, output_file):
    ## create frames for each state
    all_data = pd.read_json(input_file)

    all_data.is_copy = False
    pd.options.mode.chained_assignment = None  ## to allow references to original objects and not copies

    all_data['summary'] = [get_summary(x,1.5) for x in all_data.article_text.tolist()]

    size = all_data.shape[0]

    with open(output_file, 'w') as f:
        f.write(all_data.to_json(orient = "records"))
