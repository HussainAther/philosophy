knowledge = ["P"] # what we know

"""
Knowing one isn't a brain in a vat (BIV, biv).
Let's look at various methods of reasoning.
"""

def simplenotbiv():
    """
    Logical architechture for a simple brain in a vat argument and its effect
    on whether we have hands.
    """
    if "biv" not in knowledge: # If I don't know I'm not a biv
        return("I don't know that I have hands.")
     

"""
Pretty simple, but doesn't tell us much. Let's form a skeptical argument
about how strong the biv scenario is on our access to knowledge. 
"""

def knowP(P):
    """
    Skeptical argument for some belief or claim p on the external world. 
    If you can't be sure that you are not a brain in a vat,
    then you can't rule out the possibility all your beliefs about the external 
    world are false.
 
    Descartes outlined this method of reasoning, and this line
    of reasoning was the premise for the movie "The Matrix." 
    """
    if P in knowledge: # if we know P. Here we're using Python's 
         return("I don't know that I'm not a brain in a vat.") 
