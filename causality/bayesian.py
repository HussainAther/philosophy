"""
We can use a Bayesian approach to induce causal relationship. We look for a causal
graph that maximizes the posterior probability

p(c|D) = p(C)p(D|C) / Σp(C')p(D|C')

where D is a database of observed past case data. We solve for the integral

p(D|C) = integral of p(D|C,S_C)p(S_C)dS_C

with probability specifications S_C that accompany C in a Bayesian net.	
"""
