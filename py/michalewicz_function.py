#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Created on Sun Jan  3 20:36:24 2021

@author: thatone

Michalewicz function implementation in Python.

"""

import numpy as np
import math

def michalewicz_function(X, m = 10.0):
    """
    Parameters
    ----------
    X : array
        X vector as input in michalewicz function.
    m : flat, optional
        parameter in michalewicz function. The default is 10.

    Returns
    -------
    float        

    """
   
    X = np.asarray_chkfinite(X)
    dim = len(X)
    i = np.arange(1., dim + 1.)
    return -sum(np.sin(X) * np.sin(i * X**2 / math.pi) ** (2 * m))

if __name__ == '__main__':
    X = (2.20, 1.57)
    result = michalewicz_function(X, 10)
    if round(result, 3) != -1.801:
        raise ValueError('ERROR: Not correct.')
