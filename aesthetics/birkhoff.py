from simplicity import simplicity

"""
Mathematician George David Birkhoff created an aethetic measure M = O/C
as the ratio of order to complexity.
"""

def arrayorder(a, method="oop"):
    """
    For an array a, return its order. We use a simple, rough estimation of
    order by how sorted the array is from least to greatest.
    Methods:
        oop = Add one point for each array element that shouldn't be at the index. 
        boolean = If the array is sorted, return True. Otherwise return False.
    """
    if method == "oop":
        count = 0
        prev = a[0]
        for i in a:
            if i < prev:
                count +=1
        return count 
    elif method == "boolean":
        prev = a[0]
        for i in a:
            if i < prev:
                 return False
        return True

def birk(f, a):
    """
    Measure from Birkhoff's mathematical theory of aesthetics return the Birkhoff measure 
    for a given function f and corresponding array a.
    """
    c = 1 / simplicity(f) # For a given function f, calculate the simplicity using our 
                          # imported function. Then take the inverse to measure complexity.
    o = arrayorder(a) # A rough estimate of order using the array a.  
    return o / c
