from feature_extraction.linguistic.lexical import Lexical


class News:
    def __init__(self, text):
        self.linguistics = [Lexical(text)]

    def __str__(self):
        result = ""
        for i in self.linguistics:
            result += str(i)
        return result
