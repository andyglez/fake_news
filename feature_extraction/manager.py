from feature_extraction.news import get_features
from os import system
import numpy as np

def manage(corpus,shape):
    news = []
    for i, text in enumerate(corpus):
        news.append(get_features(text, shape))
        system('cls||clear')
        print('Processed ' + str(i) + ' ' + str(len(corpus)))
    return news

def flat_input(corpus, classes, shape):
    docs = [title + '. ' + text for title, text in corpus]
    news = manage(docs, shape)
    prep = [n for n in news]
    outp = [[1, 0] if i == 'FAKE' else [0, 1] for i in classes]
    return np.asarray(prep), np.asarray(outp)

def max_pos(l):
    m = 0
    j = 0
    for i, n in enumerate(l):
        if n > m:
            j = i
            m = n
    return j

def calculate_metrics(pred, real):
    result = []
    for p,r in zip(pred, real):
        (i, j) = (max_pos(p), max_pos(r))
        if i == j and r == [1,0]:
            result.append('TP')
        elif i == j and r == [0,1]:
            result.append('TN')
        elif i != j and r == [1,0]:
            result.append('FN')
        elif i != j and r == [0,1]:
            result.append('FP')
    precision = result.count('TP') / (result.count('TP') + result.count('FP'))
    recall = result.count('TP') / (result.count('TP') + result.count('FN'))
    f1 = 2*((precision*recall)/(precision + recall))
    accuracy = (result.count('TP') + result.count('TN')) / (result.count('TP') + result.count('TN') + result.count('FN') + result.count('FP'))
    msg = 'Precision: \t' + str(precision) + '\n'
    msg += 'Recall: \t' + str(recall) + '\n'
    msg += 'F1: \t\t' + str(f1) + '\n'
    msg += 'Accuracy: \t' + str(accuracy)
    print(msg)
