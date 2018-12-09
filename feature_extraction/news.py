import numpy as np
from math import sqrt
from nltk.tokenize import sent_tokenize as st
from feature_extraction.linguistic.lexical import Lexical
from feature_extraction.linguistic.syntactic import Syntactic
from feature_extraction.linguistic.ds import DomainSpecific

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


class News:
    def __init__(self, text, shape):
        sentences = st(text)
        self.lexical = Lexical(sentences, shape)
        self.syntactic = Syntactic(sentences, shape)
        self.ds = DomainSpecific(sentences, shape)

    def __str__(self):
        return str(self.lexical) + '\n' + str(self.syntactic) + '\n' + str(self.ds) + '\n'

    def features_to_list(self):
        result = np.asarray(self.lexical) * np.asarray(self.syntactic) * np.asarray(self.ds)
        return normal(result.tolist())
        
