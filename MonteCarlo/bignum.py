import numpy as np


def bernoulli(p, size):
    array = np.random.binomial(n=1, p=p, size=size)
    get_mean = (array.sum()) / size
    return get_mean

def poisson(meanAvar, size):

    poisson_array = np.random.poisson(meanAvar, size=size)
    get_mean = int(poisson_array.sum()) / size
    return get_mean



