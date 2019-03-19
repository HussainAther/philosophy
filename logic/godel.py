from isPeanoProof import isPeanoProof
from provableInPeano import provableInPeano
from convertHaltToPeano import convertHaltToPeano

"""
Logician Kurt Gödel proved his first incompleteness theorem in the 1930s. It can loosely be descrbied as
"there are true statements about theintegers that cant be proved from the axioms." We can' use computers to rpove all the true
statements in mathematics.

Peano arithmetic is a logical system that correspond to parts of the real world using staements about integers,
addition, and multiplication.
"""
def provableInPeano(inString):
    """
    Return "Yes" if S ASCII string that represents a statement in Peano arithmetic is provable from the axioms
    and inference rules of Peano arithmetic. Return "no" otherwise or if S is not a cloesd well-formed statement.
    """
    proofString = ""
    while True:
        if isPeanoProof(proofString, inString)=="yes":
            return "yes"
        proofString = utils.nextASCII(proofString)

def haltsViaPeano(inString):
    haltsInPA = convertHaltToPeano(inString)
    return trueInPeano(haltInPA)

def haltsViaCompletePeano(inString):
    haltInPeano = convertHaltToPeano(inString)
    notHaltInPeano = "NOT " + haltInPeano
    proofString = ""
    while True:
        if isPeanoProof(proofString, haltInPeano)=="yes":
            return "yes"
        if isPeanoProof(proofString, notHaltInPeano)=="yes":
            return "no"
        proofString = utils.nextASCII(proofString)


def godel(inString):
    godelProg = rf("godel.py")
    haltInPeano = convertHaltToPeano(godelProg)
    notHaltInPeano = "NOT " + haltInPeano
    if provableInPeano(notHaltInPeano) == "yes":
        return "halted"
    else:
        utils.loop()

