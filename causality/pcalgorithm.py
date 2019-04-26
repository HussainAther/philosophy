"""
Peter Spirtes, Clark Glymour, and Richard Scheines developed an account of causal discovery in the 
last decade of the twentieth century. Their approach was to induce a partially directed causal graph 
from independence constraints embodied in a database of past case data. Undirected edges in this graph 
indicate causal relations of unknown direction. They developed the PC algorithm (apparently named 
after its authors, Peter and Clark) to construct the graph:

1. Start off with a complete undirected graph on V.
2. For n=0,1,2,...remove any edges A−B if A⊥B|X for some set X of n neighbors of A.
3. For each structure A − B − C in the graph with A and C not adjacent, substitute A -> B <- C 
	if B was not found to screen off A and C in the previous step.
4. Repeatedly substitute
	(i) A -> B -> C for A -> B − C with A and C non-adjacent. 
	(ii) A -> B for A - B if there is a chain of arrows from A to B.
"""

def pcalg(g, n):
    """
    For some undirected graph g on V with number of neighbors n.
    """
     
