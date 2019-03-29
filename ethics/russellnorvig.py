
"""
An artificial intelligence (AI) approach to ethics can embrace many different
ideas from philosophy. In "Artificial Intelligence: A Modern Approach," (known as AIMA) 
computer scientists Peter Norvig and Stuart Russell believe we can create goals for AI
to act rationally. Russell asks "What is AI?" as "What is intelligence?" to identify intelligence
closely tied with rationality. Intelligent agents can take percepts as input and act
based upon them. We can create performance measures by calculating V the expected utility
according to the performance measure U of the agent function f that operates on E:

f_opt = max V(f, E, U)
"""

def fopt(V, E, U):
    """
    Maximize our function fopt by maximizing expected utility in the corresponding environment.
    """
    return max(V(f0, E, U))
