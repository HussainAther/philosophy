"""
Scientific realism pertains to scientific theories and the entities they postulate. A theory postulates an entity if it is expressed in terms of the properties and behavior of the entity. For example, Mendelian genetics postulates a “gene” as a unit that controls a heritable characteristic. Eventually we discovered that genes are encoded in DNA, but for about 50 years, a gene was just a postulated entity. 

We can state philosophical positions in a range of strengths, where SR1 is a weak form of scientific realism and SR4 is a strong form:
SR1: Scientific theories are true or false to the degree that they approximate reality, but no theory is exactly true. Some postulated entities may be real, but there is no principled way to say which ones.
SR2: As science advances, our theories become better approximations of reality. At least some postulated entities are known to be real.
SR3: Some theories are exactly true; others are approximately true. Entities postulated by true theories, and some entities in approximate theories, are real.
SR4: A theory is true if it describes reality correctly, and false otherwise. The entities postulated by true theories are real; others are not.

SR4 is so strong that it is probably untenable; by such a strict criterion, almost all current theories are known to be false. Most realists would accept something in the space between SR1 and SR3.
"""

def realism(t, a):
    """
    For an array of true values t and an approximate of some sort a, return how realist they are.
    This is an incredibly crude method of computing realism (if that were even possible) that
    shouldn't be used in any serious philosophical or scientific analysis.
    """
    return (set(t) * set(a))
