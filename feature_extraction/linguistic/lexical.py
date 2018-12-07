import re
from nltk.tokenize import word_tokenize as wt


def total_words(text):
    token_list = wt(text)
    result = []
    for token in token_list:
        signs = re.compile('[^a-zA-Z0-9_\\+\\-/]')
        clean_word = signs.split(token)
        for word in clean_word:
                if word != '' and not is_number(word):
                    result.append(word)
    return result


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


class Lexical:
    def __init__(self, text):
        self.words = total_words(text)
        self.total_words = int(len(self.words))
        self.avg_characters = self.__characters_per_word__()
        self.large_words = [w for w in self.words if len(w) > int(sum(self.avg_characters) / float(len(self.avg_characters)))]
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
        while len(count_per_word) < 48:
            count_per_word.append(0)
        return [v for (i, v) in enumerate(count_per_word) if i < 48]#sum(count_per_word) / float(len(count_per_word))

    def __freq_of_large_words__(self):
        freq_per_word = [self.large_words.count(w) / float(len(self.large_words)) for w in self.large_words]
        while len(freq_per_word) < 48:
            freq_per_word.append(0)
        return [v for (i, v) in enumerate(freq_per_word) if i < 48]#sum(freq_per_word) / float(len(freq_per_word))

    def contains(self, word):
        return self.large_words.count(word) > 0

    def to_list(self):
        result = [self.total_words, len(self.unique_words) // self.total_words]
        for i in self.avg_characters:
            result.append(i)
        for j in self.avg_freq:
            result.append(j)
        return result
