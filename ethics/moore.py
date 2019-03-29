"""
Philosopher James Moore believes artificial intelligence (AI) can be 
an ethical agent that is implicit (has ethical constraints programmed 
into it), explicit (can weigh inputs in a given ethical framework to
choose an action), or full agency (can make ethical judgments and 
defend its reasoning).
"""

def implicit():
    """
    An ethical agent that acts with implicit ethical constraints.
    """
    return True 

def explicit(f):
    """
    For a list of inputs f, choose an action.    
    """
    x = True
    for i in f:
        x = not x 
    return x
