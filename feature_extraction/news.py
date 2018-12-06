from feature_extraction.linguistic.lexical import Lexical
from feature_extraction.linguistic.syntactic import Syntactic


class News:
    def __init__(self, text):
        self.lexical = Lexical(text)
        self.syntactic = Syntactic(text)

    def __str__(self):
        return str(self.lexical) + '\n' + str(self.syntactic) + '\n'
