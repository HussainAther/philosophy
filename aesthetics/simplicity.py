from inspect import signature

"""
The word "simplicity" is used in very many different senses. Schrödinger’s theory, for instance,
is of great simplicity in a methodological sense, but in another sense it might well be called
"complex." We can say of a problem that its solution is not simple but difficult, or of a presentation
or an exposition that it is not simple but intricate.

"""

def simplicity(f):
    """
    Return the simplicity of some function f. We may view simplicity
    as a function of the number of paramters. In this case, we return the
    number of parameters. This is a very basic, simple method of measuring   
    simplicity (on the assumption it can be computed using object-oriented 
    programming to begin with). It's not to be taken seriously.
    """
    return signature(f)

