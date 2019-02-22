import sys
import nltk

"""
Use Natural Language Tool Kit.
Script that can analyze text for soundness and completeness in arguments.
Require user to justify claims using other claims in the text.
Create a logical map that shows how claims are justified.
Call this a justification map.
"""
file = sys.argv[1]

just = {} # justification map

with open(file, "r") as infile:
    for line in infile:

