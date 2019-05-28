"""
Turing machine implementation. (turing)
"""

class Tape(object):
    """
    Represent an object the Turing machine.
    """
    blank_symbol = " " # For printing a blank symbol on the tape
    
    def __init__(self, tape_string = ""): 
        """
        The dictionary of th turing machine is the tape that has the entries
        we print on the tape. 
        """
        self.__tape = dict((enumerate(tape_string)))
       
    def __str__(self):
        """
        Print out part of the tape as a string.
        """ 
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s