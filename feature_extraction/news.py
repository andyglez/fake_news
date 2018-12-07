from feature_extraction.linguistic.lexical import Lexical
from feature_extraction.linguistic.syntactic import Syntactic
from feature_extraction.linguistic.ds import DomainSpecific


def concat(a, b):
    aux = []
    for i in a:
        aux.append(i)
    for j in b:
        aux.append(j)
    return aux


class News:
    def __init__(self, text):
        self.lexical = Lexical(text)
        self.syntactic = Syntactic(text)
        self.ds = DomainSpecific(text)

    def __str__(self):
        return str(self.lexical) + '\n' + str(self.syntactic) + '\n' + str(self.ds) + '\n'

    def to_list(self):
        return concat(self.lexical.to_list(), concat(self.syntactic.to_list(), self.ds.to_list()))
