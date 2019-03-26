"""
Check for satisfiability.
"""

class SAT(object):
    """
    Basic and somewhat efficient way of solving satisfiability using Python. 
    """
    def addclause(self, line):
        """

        """
        clause = []
        for i in line.split(): # for each literal in the line
            n = 1 if i.startswith("~") else 0 # n means negated 
            a = i[n:] # a is the variable
            if a not in self.var_table: # if the variable is not in our variable table
                self.var_table[a] = len(self.variables)
                self.variables.append(a)
            enc = self.var_table[a] << 1 | n # bitwise shift to create enc encoded literal
