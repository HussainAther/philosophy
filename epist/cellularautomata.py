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

For Class 3 CAs, we can consider philosophical determinism in classifying our automata.
Determinism can be defined in such a way of increasing strength:
D1: Deterministic models can make accurate predictinos for some physical systems.
D2: Many physical systems can be modeled by deterministic processes, but some are
    intrinsically random.
D3: All events are casued by prior events, but many physical systems are nevertheless
    fundamentally unpredictable.
D4: All events are caused by prior events, and can (in principle) be predicted.

An example of a Class 4 CA that is Turing complete would be Wolfram's Rule 110.
In principle, any calculation can be simulated using this automata.
"""

def rule110(s,m=range(40)):
    """
    Wolfram's Rule 110 in generating interesting behavior 
    on the boundary between stability and chaos.
    """
    s=[int(i in s)for i in m]
    for g in m:print''.join([' X'[i]for i in s]);s=[int(not''.join(map(str,s[i-1:i+2]if i else s[:2]))in'111 100 000 00'.split())for i in m]

"""

"""
