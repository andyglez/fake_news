import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def reshape_vector(vector, shape):
    return fill(vector, shape) if len(vector) < shape else compress(vector, shape)

def reshape_matrix(matrix, shapeX, shapeY):
    fit = np.asarray(matrix)
    fit.resize(shapeX, shapeY, refcheck=False)
    return fit.tolist()

def fill(vector, shape):
    result = vector.copy()
    for _ in range(len(vector), shape):
        result.append(0)
    return result

def compress(vector, shape):
    aux = vector.copy()
    result = []
    if not len(vector) % shape == 0:
        aux = fill(vector, shape *((len(vector) // shape) + 1))
    k = (len(aux) // shape)
    for i in range(shape):
        val = 0
        for j in range(k):
            val += aux[i*k + j]
        result.append(val / k)
    return result