
# coding: utf-8

# In[125]:

import pandas as pd
import numpy as np
from tensorflow import keras
from math import sqrt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize as st


# In[126]:

def tf_idf(text):
    sentences = st(text)
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(sentences)
    matrix = np.asarray((tfidf * tfidf.T).A)
    matrix.resize(20, 20)
    return matrix.flatten()


# In[127]:

def flat_input(corpus, classes):
    docs = [title + '. ' + text for title, text in corpus]
    prep = [tf_idf(text) for text in docs]
    outp = [[1, 0] if i == 'FAKE' else [0, 1] for i in classes]
    return np.asarray(prep), np.asarray(outp)


# In[161]:

def max_pos(l):
    m = 0
    j = 0
    for i, n in enumerate(l):
        if n > m:
            j = i
            m = n
    return j


# In[179]:

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


# In[131]:

cols = ['ID', 'TITLE', 'TEXT', 'LABEL']
data = pd.read_csv("fake_or_real_news.csv", names=cols, header=0)


# In[132]:

k = len(data[cols[3]]) // 2
x_train, y_train = flat_input(list(zip(data[cols[1]], data[cols[2]]))[:k], data[cols[3]][:k])
x_validate, y_validate = flat_input(list(zip(data[cols[1]], data[cols[2]]))[k:], data[cols[3]][k:])


# In[262]:

model = keras.Sequential()
model.add(keras.layers.Dense(units=15, activation='relu', input_dim=400))
model.add(keras.layers.Dense(units=8, activation='relu'))
model.add(keras.layers.Dense(units=2, activation='softmax'))


# In[263]:

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True),
              metrics=['accuracy'])


# In[264]:

model.fit(x_train, y_train, epochs=10, batch_size=32)


# In[265]:

model.evaluate(x_validate, y_validate, batch_size=32)


# In[266]:

result = model.predict(x_validate, batch_size=32).tolist()


# In[267]:

c = data[cols[3]].tolist()[:k]
str(c.count('FAKE')) + ' / ' + str(c.count('REAL'))


# In[268]:

calculate_metrics(result, y_validate.tolist())


# In[ ]:



