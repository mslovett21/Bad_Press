import gensim
from gensim import corpora, models
import pyLDAvis.gensim

import nltk
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string # allows us to define punctutation to remove
from nltk.corpus import wordnet as wn # allows us to access pos types

wordnet_lemmatizer = WordNetLemmatizer()

# Tokenize text string by word
def splitToWords(text):
    return WhitespaceTokenizer().tokenize(text)

# Tokenize text string by sentence
def splitToSentences(text):
    return sent_tokenize(text)

# change words to lowercase in a list
def convertToLowercase(text):
    return [word.lower() for word in text]

# remove punctuation from the string
def removePunctuation(text):
    exclude = set(string.punctuation)
    keep_these_punct = ['%']
    for punct in keep_these_punct:
        exclude.remove(punct)
    converted_text = ''.join(ch for ch in text if ch not in exclude)
    return converted_text

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


stopset = set(nltk.corpus.stopwords.words('english'))
extra_stopwords = ["like", "it’s", "uh", "going", "that’s", "think", "actually", "kind", "…", "know", "come", "u", "really"
                   ,"mr", "june", "july", "august", "aug", "festival", "theater", "music", "concert", "dance", "performance"
                   , "jazz", "band", "arts", "art","museum","painting", "artist", "exhibition","gallery", "ms", "sculpture"
                   , "tell", "also","thats", "im", "album", "film", "movie", "opera", "cookbook", "orchestra", "play"
                   , "street", "design", "photograph", "drawing", "collection", "street", "design", "direct", "jan", "may","summer"
                   , "season", "production", "park", "oct", "show", "quartet", "series", "may"]
for word in extra_stopwords:
    stopset.add(word)

# removes stop words from a list of words
def removeStopWords(text):
    return [word for word in text if word not in stopset]

# checks if a word isnt in the stopset
def notStopWord(word):
    return word not in stopset


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
