"""
Turing machine implementation. (turing)
"""

class Tape(object):
    """
    Represent an object the Turing machine tape.
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

    def __getitem__(self, index):
        """
        Return an index from the tape.
        """
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        """
        Set a character chat at a certain position pos on the tape. 
        """
        self.__tape[pos] = char

class TuringMachine(object):
    """
    The Turing machine object.
    """
    
    def __init__(self,
        """
        Initialize the tape and the machine with the states.
        """ 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        """
        Return the tape as it is.
        """ 
        return str(self.__tape)
    
    def step(self):
        """
        Perform a step in our function.
        """
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0] 
