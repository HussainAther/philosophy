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
        
