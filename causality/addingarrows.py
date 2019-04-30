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
    result = {} # Dictionary of paths connected by arrows 
    for i in g: # for some node i, we check its connection with each other node j 
        maxweight = 0 # Set the maximum weight for this node i 
        for j in g: # Compare each node i with some other node j
            if i != j: # Exclude any paths of a node leading directly to itself 
                if g[i] - g[j] > maxweight: # If we can find a weight greater than the maximum weight 
                    result[prev] = g[i] # Update in our result dictionary
                    maxweight = g[i] - g[j] 
   return result  
