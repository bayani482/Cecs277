"""


"""
import random as rand

from door import Door


class ComboDoor(Door):
    def __init__(self):
        self._correct_code = rand.randint(1,10)
        self._input = 0
    def examine_door(self):
        return "You encounter a door with a combination lock, You can spin the dial to a number 1-10."
    def menu_options(self):
        return "Enter a number (1-10)"

    def get_menu_max(self):
        options = 10
        return options
    
    def attempts(self, option):
        self._input = option
        return f"You dialed to... {self._input}."
    
    def is_unlocked(self):
        if self._correct_code == self._input:
            return  True
        else:
            return False

    def clue(self):
        if self._input > self._correct_code:
            return "Try a lower value"
        if self._input < self._correct_code:
            return "Try a higher value"

    def success(self):
        return "You found the correct value and opened the door"

    