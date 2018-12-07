from whoosh.analysis import NgramFilter, StandardAnalyzer
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk import pos_tag, RegexpParser
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
        self.average_length_sentence = sentences_lengths(text)
        tags = [pos_tag(words) for words in [wt(sent) for sent in st(text)]]
        a = 0
        parser = RegexpParser('''
                            PHRASES: {<DT>* <NNP> <NNP>+}
                            ''')
        self.frequency_word_functions = self.__frequency_word_functions(tags, parser)

    def __frequency_word_functions(self, tags, parser):
        phrases = []
        for tagged_n_gram in tags:
            chunks = parser.parse(tagged_n_gram)
            for sub in chunks.subtrees(filter=lambda t: t.label() == 'PHRASES'):
                phrases.append(' '.join([i[0] for i in sub]))
        freq = [phrases.count(p) for p in phrases]
        return sum(freq) / float(len(freq)) if not len(freq)   0 else 0

    def __str__(self):
        result = 'Average Length Sentences: ' + str(self.average_length_sentence) + '\n'
        result += 'Average Phrases Frequency: ' + str(self.frequency_word_functions)
        return result
