import numpy as np
from math import sqrt
from nltk.tokenize import sent_tokenize as st
from feature_extraction.linguistic.lexical import get_lexical_features
from feature_extraction.linguistic.syntactic import get_syntactic_features
from feature_extraction.linguistic.ds import tf_idf

def normal(matrix):
    return np.transpose([normalize(i) for i in np.transpose(matrix)])

def normalize(weights):
    den = normal_denominator(weights)
    return [w / den for w in weights]

def normal_denominator(weights):
    den = 1
    for x in [pow(w, 2) for w in weights]:
        den += x
    return sqrt(den)

def get_features(text, shape):
    sentences = st(text)
    lexical = get_lexical_features(sentences, shape)
    syntactic = get_syntactic_features(sentences, shape)
    ds = tf_idf(sentences, shape)
    aux = np.asarray(lexical) + np.asarray(syntactic) + np.asarray(ds)
    return np.asarray(normal(aux)).flatten()
