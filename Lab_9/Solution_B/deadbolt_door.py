"""
deadbolt class

"""

import random as rand

from door import Door


class Deadbolt(Door):
    """
    Deadbolt door is a subclass of door that toggle two bolts
    Args:
        Door (object):  create a object of door
    """
    def __init__(self):
        """
        initializes values of deadbolt door
        _bolt1 (int): The current state of the door 1
        _bolt2 (int): The current state of the door 2
        """
        self._bolt1 = rand.randint(1,2)
        self._bolt2 = rand.randint(1,2)
    def examine_door(self):
        """
        returns a string representation of the door
        Returns:
            str: message describing the door
        """
        return "You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked"

    def menu_options(self):
        """
        returns a string representation of the menu options
        Returns:
            str: message describing the options you can interact with the door
        """
        return "1. Toggle bolt 1\n2. Toggle bolt 2"

    def get_menu_max(self):
        """
        returns a int value of the menu options
        Returns:
            int: returns the int value of the max menu options
        """
        options = 2
        return options
    
    def attempts(self, option):
        """
        a function that takes in user input and tries to unlock the door

        Args:
            option (int): a int value of the menu selection

        Returns:
            str: a message describing what happens after the user selects an option
        """
        self._input = option
        match self._input:
            case 1:
                
                if self._bolt1 == 1:
                    self.bolt1 = 2
                elif self._bolt1 == 2:
                    self._bolt1 = 1
                return "You toggle the first bolt"
            case 2:
                
                if self._bolt2 == 1:
                    self._bolt2 = 2
                elif self._bolt2 == 2:
                    self._bolt2 = 1
                return "You toggle the second bolt"
        if self._bolt1 == 1 and self._bolt2 == 1:
            self.success()

    def is_unlocked(self):
        """
        returns true of false of the current state of the door

        Returns:
            bool: if the door is locked or unlocked
        """
        if self._bolt1 == 1 and self._bolt2 == 1:
            return True
        else:
            return False

    def clue(self):
        """
        Gives the user a clue on how to unlock the door

        Returns:
            str: string representation of how to unlock the door
        """
        if self._bolt1 == 2 and self._bolt2 == 2:
            return "You jiggle the door... it's completely locked."
        else: #(self._bolt1 == 1 and self._bolt2 == 2) or (self._bolt1 == 2 and self._bolt2 == 1)
            return "You jiggle the door... it seems like one of the bolts is unlocked."

    def success(self):
        """
        string representation if they unlock the door

        Returns:
            str: message of congratulations
        """
        return "You unlocked both deadbolts and opened the door"
    
    
