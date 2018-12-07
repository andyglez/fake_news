import pandas as pd
from feature_extraction import manager
from nltk import ngrams
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk.cluster.util import cosine_distance
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import math

def tf_idf(text):
    sentences = st(text)
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(sentences)
    matrix = np.asarray((tfidf * tfidf.T).A)
    matrix.resize(50, 50)
    return matrix.flatten()

cols = ['ID', 'TITLE', 'TEXT', 'LABEL']
data = pd.read_csv("fake_or_real_news.csv", names=cols, header=0)
#news = manager.manage(data, cols[1:len(cols)-1])
#classes = manager.classes(data, cols[-1])

s = data[cols[1]][0] + '. ' + data[cols[2]][0]
r = tf_idf(s)
print(r.shape)
print(r)
#total = len(data[cols[-1]])


