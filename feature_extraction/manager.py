from feature_extraction.news import News
from os import system
from math import sqrt
from numpy import transpose

def manage(data, names):
    news = []
    total = len(data[names[0]])
    corpus = []
    for i in range(total):
        aux = ""
        for j in names:
            aux += data[j][i] + "."
        corpus.append(aux)
    for i, text in enumerate(corpus):
        news.append(News(text))
        system('cls||clear')
        print('Processed ' + str(i) + ' ' + str(total))
    return news


def classes(data, name):
    result = []
    for i in data[name]:
        if i == 'FAKE':
            result.append([1, 0])
        else:
            result.append([0, 1])
    return result

def normal(matrix):
    return transpose([normalize(i) for i in transpose(matrix)])

def normalize(weights):
    den = normal_denominator(weights)
    return [w / den for w in weights]


def normal_denominator(weights):
    den = 1
    for x in [pow(w, 2) for w in weights]:
        den += x
    return sqrt(den)