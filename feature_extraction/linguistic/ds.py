from collections import Counter
from nltk.cluster.util import cosine_distance
from utils import reshape_matrix, reshape_vector
from sklearn.feature_extraction.text import TfidfVectorizer

def buildVector(iterable1, iterable2):
    counter1 =  Counter(iterable1)
    counter2= Counter(iterable2)
    all_items = set(counter1.keys()).union( set(counter2.keys()) )
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def calculate_cosine_distance(sentences, shape):
    result = []
    for i in sentences:
        for j in sentences:
            v1, v2 = buildVector(i, j)
            result.append(cosine_distance(v1, v2))
    return reshape_matrix(reshape_vector(result, shape), shape, shape)

def tf_idf(sentences, shape):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(sentences)
    return reshape_matrix((tfidf * tfidf.T).A, shape, shape)

class DomainSpecific:
    def __init__(self, sentences, shape):
        self.cosine_distance = calculate_cosine_distance(sentences, shape)
        self.tfidf = tf_idf(sentences, shape)
    
    def __str__(self):
        return str(self.tfidf)
