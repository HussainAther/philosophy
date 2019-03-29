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

def birk(o, c):
    """
    Measure from Birkhoff's mathematical theory of aesthetics.
    """
    return o / c
    
