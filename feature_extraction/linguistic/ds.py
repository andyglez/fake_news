from nltk import ngrams
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk.cluster.util import cosine_distance
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import math


def all_grams(text):
    sentences = st(text)
    return [ngrams(wt(sent), len(sentences[0]) // 4) for sent in sentences]

def buildVector(iterable1, iterable2):
    counter1 =  Counter(iterable1)
    counter2= Counter(iterable2)
    all_items = set(counter1.keys()).union( set(counter2.keys()) )
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def calculate_cosine_distance(text):
    sentences = st(text)
    result = []
    for i in sentences:
        for j in sentences:
            v1, v2 = buildVector(i, j)
            result.append(cosine_distance(v1, v2))
    while len(result) < 100:
        result.append(0)
    return [v for i, v in enumerate(result) if i < 100]

def tf_idf(text):
    sentences = st(text)
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(sentences)
    matrix = np.asarray((tfidf * tfidf.T).A)
    matrix.resize(50, 50)
    return matrix



class DomainSpecific:
    def __init__(self, text):
        self.quotes = (text.count("\'") + text.count("\"")) // 2
        self.links = text.count('http') // 2
        self.cosine_distance = calculate_cosine_distance(text)
    
    def __str__(self):
        result = 'Total Quoted Phrases: ' + str(self.quotes) + '\n'
        result += 'Total Link Count: ' + str(self.links)
        return result

    def to_list(self):
        result = [self.quotes, self.links]
        for i in self.cosine_distance:
            result.append(i)
        return result
