import re
from feature_extraction.linguistic.utils import reshape_matrix, reshape_vector
from nltk.tokenize import word_tokenize as wt


def total_words(sentences):
    result = []
    for s in sentences:
        l = []
        token_list = wt(s)
        for token in token_list:
            signs = re.compile('[^a-zA-Z0-9_\\+\\-/]')
            clean_word = signs.split(token)
            for word in clean_word:
                if word != '' and not is_number(word):
                    l.append(word)
        result.append(l)
    return result

def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False

def get_lexical_features(sentences, shape):
    return reshape_matrix([reshape_vector([s.count(w) / len(s) for w in s], shape) for s in total_words(sentences)], shape, shape)
