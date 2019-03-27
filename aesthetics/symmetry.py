import sys
import numpy as np

"""
We find symmetry as it relates to beauty and aesthetics throughout
mathematics and science.

Usage:

'python symmetry.py inputfile'
"""

lengths = [] # length of each line
matr = [] # matrix of the file's content 

with open(sys.argv[1]) as file: # open up some file the user inputs
    for line in file:
        lengths.append(len(line)) # append the length of each line
        matr.append(line.split()) # append each line in split form to our matrix

matr = np.array(matr)
