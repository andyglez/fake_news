from feature_extraction.linguistic.lexical import Lexical


class News:
    def __init__(self, text):
        self.lexical = Lexical(text)

    def __str__(self):
        return str(self.lexical) + '\n'
