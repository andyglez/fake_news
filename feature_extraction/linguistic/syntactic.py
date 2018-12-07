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


def frequency_word_functions(tags, parser):
    phrases = []
    for tagged in tags:
        chunks = parser.parse(tagged)
        for sub in chunks.subtrees(filter=lambda t: t.label() == 'PHRASES'):
            phrases.append(' '.join([i[0] for i in sub]))
    freq = [phrases.count(p) for p in phrases]
    return sum(freq) / float(len(freq)) if not len(freq) == 0 else 0


class Syntactic:
    def __init__(self, text):
        self.average_length_sentence = sentences_lengths(text)
        tags = [pos_tag(words) for words in [wt(sent) for sent in st(text)]]
        parser = RegexpParser('''
                            PHRASES: {<DT>* <NNP> <NNP>+}
                            ''')
        self.frequency_word_functions = frequency_word_functions(tags, parser)

    def __str__(self):
        result = 'Average Length Sentences: ' + str(self.average_length_sentence) + '\n'
        result += 'Average Phrases Frequency: ' + str(self.frequency_word_functions)
        return result

    def to_list(self):
        return [self.average_length_sentence, self.frequency_word_functions]
