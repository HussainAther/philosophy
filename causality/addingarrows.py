"""
There are many ways to find a net within an approximation subspace with
maximum or close to maximum weight. The simplest is a greedy adding-arrows
algorithm:
   
Start with a discrete net (graph with no arrows), and, at each stage,
   find and weigh the arrows whose addition would ensure that the net
   remains acyclic and within the chosen subspace, and add one maximum 
   weight.
 
If more than one maximum weight arrow exists, we can spawn several new 
   nets by adding each maximum weight to the previous graph, and we can
   constantly prune the nets under consideration by eliminating those
   which no longer have maximum total weight.

We stop when no more arrows can be added and output the resulting Bayesian nets. 
"""

def weight(paths):
    """
    Weigh a list of paths to determine which net is the most optimal.
    """
    return max(paths) 

def aaa(g):
    """
    Adding-arrows algorithm on graph g (dictionary of nodes connected to edges)
    that is a discrete net (having no arrows).
    """
    result = {}
    prev = g[0] # Set the previous path 
    prevweight = 0
    for i in g:
        if g[i] - prev > prevweight: 
            result[prev] = g[i]  
        prev = g[i]
   return result  
