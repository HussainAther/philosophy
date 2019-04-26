"""
There are many ways to find a net within an approximation subspace with
maximum or close to maximum weight. The simplest is a greedy adding-arrows
algorithm:
1. Start with a discrete net (graph with no arrows), and, at each stage,
    find and weigh the arrows whose addition would ensure that the net
    remains acyclic and within the chosen subspace. 
"""
