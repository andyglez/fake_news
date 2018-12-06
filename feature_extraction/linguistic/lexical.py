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
        self.total_words = int(len(self.words))
        self.avg_characters = self.__characters_per_word__()
        self.large_words = [w for w in self.words if len(w) > int(self.avg_characters)]
        self.avg_freq = self.__freq_of_large_words__()
        self.unique_words = [w for w in self.large_words if self.large_words.count(w) == 1]

    def __str__(self):
        result = 'Total Words: %d\n' % self.total_words
        result += 'Total Unique Words: %s\n' % str(len(self.unique_words))
        result += 'Average Character Length: %s\n' % str(self.avg_characters)
        result += 'Average Word Frequency: %s' % str(self.avg_freq)
        return result

    def __characters_per_word__(self):
        count_per_word = [int(len(w)) for w in self.words]
        return sum(count_per_word) / float(len(count_per_word))

    def __freq_of_large_words__(self):
        freq_per_word = [self.large_words.count(w) / float(len(self.large_words)) for w in self.large_words]
        return sum(freq_per_word) / float(len(freq_per_word))

    def contains(self, word):
        return self.large_words.count(word) > 0