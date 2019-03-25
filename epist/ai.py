import numpy as np

"""
Addressing epistemological problems brought upon by artifiical intelligence.
Let's begin by introducing an AI that makes a simple action by how the opponent behaves.
"""

import random

class AI():
    """
    This AI will choose to defect or cooperate depending on
    the opponents past moves.
    """
    def step(self, history, round):
        # Random choice to start
        if (round == 0) or (round == 1):
            action = random.randint(0, 1)
        # If the last three moves are the same, defect
        elif sum(history[not self.order][round-4:round-1])/3 == (1 or 0):
            action = 0
        # Else, do what they did two moves ago
        else:
            action = history[not self.order][round - 2]
        return action 


"""
According to Moore's autoepistemic logic, modal theories of logic 
can be pursued for certain epistemic interpretations based on the concept
that a default rule as one that licenses a conclusion for a reasoning agent unless something
that the agent knows blocks the conclusion. An extension E of such theory T is a superset of T
that is stable (deductively closed) if it satisfies the following two rules:

1. If A∈E then □A∈E.
2. If A∉E then ¬□A∈E.
"""


