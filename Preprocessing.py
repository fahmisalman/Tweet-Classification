from nltk.stem.wordnet import WordNetLemmatizer
import re
# from nltk.stem.porter import *


def caseFolding(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z]', ' ', sentence)
    return sentence


def tokenization(sentence):
    return sentence.split()


def lemmatization(token):
    lemma = WordNetLemmatizer()
    temp = []
    for i in range(len(token)):
        temp.append(lemma.lemmatize(token[i]))
    return temp


def stopwordRemoval(token):
    stopword = [line.rstrip('\n\r') for line in open('stopwords_en.txt')]
    temp = []
    for i in range(len(token)):
        if token[i] not in stopword:
            temp.append(token[i])
    return temp