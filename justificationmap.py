import sys
import codecs
import nltk
from nltk.collocations import *

nltk.download("genesis")

"""
Use Natural Language Tool Kit.
Script that can analyze text for soundness and completeness in arguments.
Require user to justify claims using other claims in the text.
Create a logical map that shows how claims are justified.
Call this a justification map.
"""
file = codecs.open("/Users/syedather/Desktop/thoughts.txt", "r", "utf-8-sig")
# file = open("/Users/syedather/Desktop/thoughts.txt", "r")

text = file.read()

just = {} # justification map

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(nltk.corpus.genesis.words(file))
finder.nbest(bigram_measures.pmi, 10)
