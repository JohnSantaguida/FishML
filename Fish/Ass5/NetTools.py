import numpy as np

def sigmoid(num):
    denom = 1.0+np.exp(-1*num)
    return 1.0/denom

def sigmoid_deriv(num):
    val = sigmoid(num) * (1-sigmoid(num))
