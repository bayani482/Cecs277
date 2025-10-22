"""
combo door class

"""
import random as rand

from door import Door


class ComboDoor(Door):
    """
    Combo door is a subclass of door that can select up to 10 combinations
    Args:
        Door (object):  create a object of door
    """
    def __init__(self):
        """
        initializes values of deadbolt door
        _correct_code (int): the correct comination number
        __input (int): user intput
        """
        self._correct_code = rand.randint(1,10)
        self._input = 0
    def examine_door(self):
        """
        returns a string representation of the door
        Returns:
            str: message describing the door
        """
        return "You encounter a door with a combination lock, You can spin the dial to a number 1-10."
    def menu_options(self):
        """
        returns a string representation of the menu options
        Returns:
            str: message describing the options you can interact with the door
        """
        return "Enter a number (1-10)"

    def get_menu_max(self):
        """
        returns a int value of the menu options
        Returns:
            int: returns the int value of the max menu options
        """
        options = 10
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
        return f"You dialed to... {self._input}."
    
    def is_unlocked(self):
        """
        returns true of false of the current state of the door

        Returns:
            bool: if the door is locked or unlocked
        """
        if self._correct_code == self._input:
            return  True
        else:
            return False

    def clue(self):
        """
        Gives the user a clue on how to unlock the door

        Returns:
            str: string representation of how to unlock the door
        """
        if self._input > self._correct_code:
            return "Try a lower value"
        if self._input < self._correct_code:
            return "Try a higher value"

    def success(self):
        """
        string representation if they unlock the door

        Returns:
            str: message of congratulations
        """
        return "You found the correct value and opened the door"

    