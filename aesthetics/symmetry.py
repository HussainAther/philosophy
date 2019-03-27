import sys
import numpy as np

"""
We find symmetry as it relates to beauty and aesthetics throughout
mathematics and science.

Usage:

'python symmetry.py inputfile'
"""

def tran(m): # Return the tranpose of some square matrix m
    tr = [] # tranpose to be returned
    n = m.shape[0] # get the side length of the matrix m
    

lengths = [] # length of each line
matr = [] # matrix of the file's content 

with open(sys.argv[1]) as file: # open up some file the user inputs
    for line in file:
        lengths.append(len(line)) # append the length of each line
        matr.append(line.split()) # append each line in split form to our matrix

matr = np.array(matr)
