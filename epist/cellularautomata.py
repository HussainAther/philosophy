"""
Stephen Wolfram believes cellular automata (CAs) can be grouped into
four classes based on their behavior. 

Class 1 is the simplest in which CAs evolve from almost any starting
    condition to the same uniform pattern.
Class 2 generates a simple pattern with nested structure such that
    the pattern contains many smaller versions of itself. Some Class 2
    CAs can generate patterns that are intricate and beautiful, and still
    simple.
Class 3 has randomness.
Class 4 are common in the natural world.
"""

def rule50(s):
    """
    Wolfram's Rule 50 is a CA that determines how a system evolves in
    time based on the notion of a 'neighborhood' which is the set of cells
    that determines the next state of a given cell. Wolfram's experiments
    used a 3-cell neighborhood with the left and right neighors.

    In the experiments, the cells had two states (0 and 1) in binary form.
   
    For some number s, we return the list of terms (that can be converted to 
    binary) resulting from Wolfram's Rule 50.
    """
    result = []
    for i in range(s):
        result.append((1/3)*(4**(i+1)-1))
    return result

"""
Wolfram's Rule 50 is an example of Class 2 cellular automata. It generates a simple pattern
with a nested structure, as described above.
"""
