from whoosh.analysis import NgramFilter, StandardAnalyzer
from nltk.tokenize import sent_tokenize as st
import re


def total_sentences(text):
    token_list = st(text)
    result = []
    for token in token_list:
        all_language_signs = re.compile('[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013\n]|\\s\\-\\s')
        clean_word = all_language_signs.split(token)
        for word in clean_word:
                if word != '':
                    result.append(word)
    return result


def sentences_lengths(text):
    lens = [len(sent) for sent in total_sentences(text)]
    return sum(lens) / float(len(lens))


class Syntactic:
    def __init__(self, text):
        self.text = text
        self.average_length_sentence = sentences_lengths(text)
        average = self.average_length_sentence
        analyzer = StandardAnalyzer() | NgramFilter(minsize=average - 1, maxsize=average + 1)
        self.tokens = analyzer(text)

    def __freq_function_words__(self, text):
        freq = [text.count(tok.text) for tok in self.tokens]
        return sum(freq) / float(len(freq))

    def __str__(self):
        return 'Average Length Sentences: ' + str(self.average_length_sentence)
