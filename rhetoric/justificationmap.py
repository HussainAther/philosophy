import sys
import codecs
import nltk

from nltk.collocations import *

"""
Use Natural Language Tool Kit.
Script that can analyze text for soundness and completeness in arguments.
Require user to justify claims using other claims in the text.
Create a logical map that shows how claims are justified.
Call this a justification map.
Check how frequently words are used with one another.
"""
file = codecs.open("/Users/syedather/Desktop/thoughts.txt", "r", "utf-8-sig")

# Tokenize the file of all the words and grammar characters.
text = file.read()
a = nltk.word_tokenize(text)

just = {} # justification map

# Collocations to figure out where multiple words commonly occur together.
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(a)
# Print the top ten bigram collocations in the text
finder.nbest(bigram_measures.pmi, 10)
# print(finder.nbest(bigram_measures.pmi, 10))

# They may be highly collocated, but they're very infrequent.
# Let's use a filter to ignore all bigrams which occur fewer than three times in the text.
finder.apply_freq_filter(3)
print(finder.nbest(bigram_measures.pmi, 10))

"""
        w1    ~w1
     ------ ------
 w2 | n_ii | n_oi | = n_xi
     ------ ------
~w2 | n_io | n_oo |
     ------ ------
     = n_ix        TOTAL = n_xx
"""

# Student's t-test
print('%0.4f' % bigram_measures.student_t(8, (15828, 4675), 14307668))

# Chi-square
print('%0.2f' % bigram_measures.chi_sq(8, (15828, 4675), 14307668))

# Likelihood ratios
print('%0.2f' % bigram_measures.likelihood_ratio(110, (2552, 221), 31777))

# Pointwise Mutual information
print('%0.2f' % bigram_measures.pmi(20, (42, 20), 14307668))
