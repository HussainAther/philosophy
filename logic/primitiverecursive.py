from math import factorial

"""
A p.r. (primitive recursive function f must be specifiable by a chain of definitions by recursion and
composition leading back ultimately to initial functions. But

(a) the initial functions S (factorial function),
Z (zero function), and Iik (identity function for i and k) are trivially computable.

(b) The composition of two computable functions g and h is computable (you just feed the output from
whatever computer routine evaluates g as input into the routine that evaluates h). And

(c) – the key point – if g and h are computable, and f is defined by primitive recursion from g and h,
then f is computable too. So as we build up longer and longer chains of definitions for p.r. functions,
we always stay within the class of computable functions.
"""

def f1(n):
    """
    Primitive recursive function for evaluating the factorial function.
    """
    fact = factorial(0)
    for y in range(0, n):
        fact = (fact*factorial(0))
    return fact

