# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:02:19 2018

@author: Shreyansh Agrawal
"""
"""
Schrodinger.py
contains functions for solving the finite differential equation
"""

import numpy as np

#function to create the Kinetic energy matrix
def Kinetic(n, diag):
    A = np.zeros((n,n),dtype=float)
    np.fill_diagonal(A,diag/2)
    for i in range(n-1):
        A[i][i+1] = -1
    A = np.divide(np.add(A,A.T),2.0)
    return A


