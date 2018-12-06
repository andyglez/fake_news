from feature_extraction.news import News


def manage(data, names):
    news = []
    total = len(data[names[0]])
    corpus = []
    for i in range(total):
        aux = ""
        for j in names:
            aux += data[j][i] + "."
        corpus.append(aux)
    for text in corpus:
        news.append(News(text))
    return news