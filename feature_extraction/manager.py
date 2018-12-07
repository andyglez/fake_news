from feature_extraction.news import News
from os import system


def manage(data, names):
    news = []
    total = len(data[names[0]])
    corpus = []
    for i in range(total):
        aux = ""
        for j in names:
            aux += data[j][i] + "."
        corpus.append(aux)
    for i, text in enumerate(corpus):
        news.append(News(text))
        system('cls||clear')
        print('Processed ' + str(i) + ' ' + str(total))
    return news


def classes(data, name):
    result = []
    for i in data[name]:
        if i == 'FAKE':
            result.append([1, 0])
        else:
            result.append([0, 1])
    return result
