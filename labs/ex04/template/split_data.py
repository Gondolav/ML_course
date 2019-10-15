# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    num_row = y.shape[0]
    indices = np.random.permutation(num_row)
    
    index_split = int(np.floor(ratio * num_row))
    index_train = indices[:index_split]
    index_test = indices[index_split:]

    x_train = x[index_train]
    x_test = x[index_test]
    y_train = y[index_train]
    y_test = y[index_test]
    
    return x_train, x_test, y_train, y_test
