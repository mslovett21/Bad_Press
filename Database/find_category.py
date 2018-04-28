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



def find_categories_and_top20(corpus, words_to_remove):
    corpus_sentences = [sent_tokenize(x) for x in corpus]
    corpus_words = []
    for x in corpus_sentences:
        corpus_words.append(([lemmatizeWords(convertToLowercase(removePunctuation(y).split())) for y in x]))
    #corpus_words = [removeStopWords(WhitespaceTokenizer().tokenize(x)) for x in corpus]

    final_corpus = []
    for x in corpus_words:
        final_corpus.append([item for sublist in x for item in removeStopWords(sublist, words_to_remove) if item.isalpha()])

    return final_corpus

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
