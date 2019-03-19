"""
With Peano arithmetic, we can write various schemas.

Its axioms – eliminating the redundancy from our original statement of the axioms – 
are the following sentences (closed well-formed formula)
"""

def axiom1(x);
    if 0 in x:
        return False
    return True

def axiom2(x, y):
    result = []
    for i in x:
        for j in y:
            if i == j:
                result.append([i, j])
    return result

def axiom3(x):
    if x + 0 == x:
        return True
    return False

def axiom4(x, y):
    pass

def axiom5(x):
    for i in x:
        if i * 0 != 0:
            return False
    return True

def axiom6(x, y):
    pass
