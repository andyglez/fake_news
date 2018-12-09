import numpy as np

def reshape_vector(vector, shape):
    fit = np.asarray(vector)
    fit.resize(shape)
    return fit.tolist()

def reshape_matrix(matrix, shapeX, shapeY):
    fit = np.asarray(matrix)
    fit.resize(shapeX, shapeY)
    return fit.tolist()