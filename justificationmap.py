import sys
import codecs
import nltk

"""
Use Natural Language Tool Kit.
Script that can analyze text for soundness and completeness in arguments.
Require user to justify claims using other claims in the text.
Create a logical map that shows how claims are justified.
Call this a justification map.
"""
file = codecs.open("/Users/syedather/Desktop/thoughts.txt", "r", "utf-8-sig")

text = file.read()
a = nltk.word_tokenize(text)

just = {} # justification map



