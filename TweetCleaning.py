import csv
import re


def at_removal(sentence):
    x = sentence.split()
    i = 0
    length = len(x)
    while i < len(x):
        if re.search('@', x[i]):
            x.pop(i)
            length -= 1
            i -= 1
        i += 1
    result = ' '.join(x)
    return result


def hashtag_removal(sentence):
    x = sentence.split()
    i = 0
    length = len(x)
    while i < len(x):
        if re.search('#', x[i]):
            x.pop(i)
            length -= 1
            i -= 1
        i += 1
    result = ' '.join(x)
    return result


def url_removal(sentence):
    x = sentence.split()
    i = 0
    length = len(x)
    while i < len(x):
        if re.search('http', x[i]):
            x.pop(i)
            length -= 1
            i -= 1
        i += 1
    result = ' '.join(x)
    return result
