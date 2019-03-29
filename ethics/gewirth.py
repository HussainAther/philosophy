import numpy as np

"""
Philosopher Alan Gewirth is known for ethical rationalism with his moral principle
the "Principle of Generic Consistency" (PCG, pgc). Every agent must act
in accodrance with his/her own and all other agents' generic rights.
For prospective purposive agents (PPA) we can derive claims.   
"""

def pgc():
    """
    For some PPA we outline its irght to freedom and well-being.
    """
    c = np.random.random() # arbitrarily chosen context
    i = np.random.random() # arbitrarily chosen individual 
