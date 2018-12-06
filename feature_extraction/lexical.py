import re
from nltk.tokenize import sent_tokenize as st


def total_words(text):
    token_list = st(text)
    result = []
    for token in token_list:
        all_language_signs = re.compile('[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013\n]|\\s\\-\\s')
        clean_word = all_language_signs.split(token)
        for clean in clean_word:
            for word in clean.split():
                if word != '':
                    result.append(word)
    return result


class Lexical:

    def __init__(self, text):
        self.words = total_words(text)
        self.total_words = self.words.__len__()

    def characters_per_word(self):
        count_per_word = [w.__len__() for w in self.words]
        sums = 0
        for v in count_per_word:
            sums += v
        return sums / count_per_word.__len__()
            

