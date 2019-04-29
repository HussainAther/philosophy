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
Its epistemic limits can be explored. This program is deterministic in the sense that 
its outcomes can be predicted as the same output depending on input when we have 
knowledge of what the input is and its nature. However, it's dependence on user input
to study the user's past moves make it somewhat non-deterministic.  
"""


