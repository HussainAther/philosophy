import sys
import nltk
from ntlk.collocations import *

"""
Use Natural Language Tool Kit.
Script that can analyze text for soundness and completeness in arguments.
Require user to justify claims using other claims in the text.
Create a logical map that shows how claims are justified.
Call this a justification map.
"""
file = "/Users/Desktop/thoughts.txt"

just = {} # justification map

with open(file, "r") as infile:
    for line in infile:
        pass

bigram_measures = mltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(nltk.corpus.genesis.words(file))
finder.nbest(bigram_measures.pmi, 10) 
