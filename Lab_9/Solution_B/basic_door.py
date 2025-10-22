"""
basic_door class

"""
import random as rand

from door import Door


class BasicDoor(Door):
    """
    Basic door is a subclass of door that can be pushed or pulled
    Args:
        Door (object):  create a object of door

    """
    def __init__(self):
        """
        initializes values of basic door
        _input (int): The user input
        _state (int): The current state of the door
        """
        self._input = 0
        self._state = rand.randint(1,2)
    def examine_door(self):
        """
        returns a string representation of the door
        Returns:
            str: message describing the door
        """
        return "You encounter a basic door, you can either push it or pull it to open."

    def menu_options(self):
        """
        returns a string representation of the menu options
        Returns:
            str: message describing the options you can interact with the door
        """
        return "1. Push\n2. Pull"

    def get_menu_max(self):
        """
        returns a int value of the menu options
        Returns:
            int: returns the int value of the max menu options
        """
        options = 2
        return options
    
    def attempts(self, option):
        """_
        a function that takes in user input and tries to unlock the door

        Args:
            option (int): a int value of the menu selection

        Returns:
            str: a message describing what happens after the user selects an option
        """
        self._input = option
        match self._input:
            case 1:
                return("you pushed the door.")
            case 2:
                return("you pulled the door.")
        if self.is_unlocked() == True:
            self.success()
        else:
            self.clue()

    def is_unlocked(self):
        """
        returns true of false of the current state of the door

        Returns:
            bool: if the door is locked or unlocked
        """
        if self._input == self._state:
            return True
        else:
            return False

    def clue(self):
        """
        Gives the user a clue on how to unlock the door

        Returns:
            str: string representation of how to unlock the door
        """
        return "Try the other way."

    def success(self):
        """
        string representation if they unlock the door

        Returns:
            str: message of congratulations
        """
        return "Congratulations, You opened the basic door."

