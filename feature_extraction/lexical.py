import re
from nltk.tokenize import sent_tokenize as st


def count_total_words(text):
    return total_words(text).__len__()

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
            

