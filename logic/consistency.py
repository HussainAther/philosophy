
"""
A consistency check procedure that may be used in logic solvers.
"""

def consistent(h, phi):
    """
    Check graph h for consistency for some formula phi.
    """
    for n in h: # for each node in h
        if phi(n) in h and phi(n) not in h:
            return False
    return True
