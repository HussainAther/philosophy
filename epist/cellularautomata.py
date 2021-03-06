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
    
    It has the following set of rules:

    Current pattern | New state	
    111 | 0	
    110	| 1
    101	| 1
    100	| 0
    011	| 1
    010	| 1
    001	| 1
    000 | 0
    """
    s=[int(i in s)for i in m]
    for g in m:print''.join([' X'[i]for i in s]);s=[int(not''.join(map(str,s[i-1:i+2]if i else s[:2]))in'111 100 000 00'.split())for i in m]

"""
Turing machine is a 1-D CA inifnite in both directions. It records the state of the
machine and acts based on a table of rules.

Every reasonable model of computation is Turing complete. This lead to the Church-Turing
Thesis which (in rough, informal language) defined what it meant to be computable.
"""

"""
Conway's Game of Life is an example of 2-D CA 

Each cell has two states—live and dead—and 8 neighbors—north, south, east, west, and the four diagonals. This set of neighbors is sometimes called a Moore neighborhood.
The rules of GoL are totalistic, which means that the next state of a cell depends on the number of live neighbors only, not on their arrangement. The following table summarizes the rules:

Number of neighbors | Current state | Next state
2–3  | live | live
0–1, 4–8 | live | dead
3  | dead | live
0–2,4–8 | dead | dead

This is further explored in conwaygameoflife.py.

Stephen Wolfram's Principle of Computational Equivalence:
Almost all processes that are not obviously simple can be viewed as computations of equivalent sophistication.
"""

"""
Rule 30 is considered to be chaotic enough to generate good pseudo-random numbers. 
As a matter of fact, rule 30 is used by the Mathematica software for its default random number generator.

The purpose of this task is to demonstrate that we show the ten first bytes that emerge from this recommendation. Start with a 
state of all cells but one equal to zero, and follow the evolution of the particular cell whose state was initially one. 
Then regroup those bits by packets of eight, reconstituting bytes with the first bit being the most significant.
"""

def eca_wrap(cells, rule):
    """
    The ends of cells wrap around for Wolfram's rules.
    """
    lencells = len(cells)
    rulebits = "{0:08b}".format(rule)
    neighbours2next = {tuple("{0:03b}".format(n)):rulebits[::-1][n] for n in range(8)}
    c = cells
    while True:
        yield c
        c = "".join(neighbours2next[(c[i-1], c[i], c[(i+1) % lencells])] for i in range(lencells))

def rule30bytes(lencells=100):
    """
    We wrap the ends of our cells as we perform Rule 30 on a lenth of cells lencells.
    """
    cells = "1" + "0" * (lencells - 1)
    gen = eca_wrap(cells, 30)
    while True:
        yield int("".join(next(gen)[0] for i in range(8)), 2))
