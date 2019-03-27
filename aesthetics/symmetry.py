import sys
import numpy as np

"""
We find symmetry as it relates to beauty and aesthetics throughout
mathematics and science.

Usage:

'python symmetry.py i m'

in which i is the input file and m is the method (1 or 2).
Method 1 is for reading in an input file line by line and 2
is for some data separated by some delimiter (such as a tab or comma). 
"""

def tran(m): # Return the tranpose of some square matrix m
    tr = [] # tranpose to be returned
    n = m.shape[0] # get the side length of the matrix m
    for i in range(n):
         for j in range(n):
             tr[i][j] = m[j][i]
    return tr
    
lengths = [] # length of each line
matr = [] # matrix of the file's content 

# Method 1: read in file line-by-line
with open(sys.argv[1]) as file: # open up some file the user inputs
    for line in file:
        lengths.append(len(line)) # append the length of each line
        matr.append(line.split()) # append each line in split form to our matrix

matr = np.array(matr)

# Method 2: convert some data set into a 2D array
s = open(sys.argv[1]).read().split() # split the input data into some split data s
matr = np.array(s, dtype=np.uint8)
