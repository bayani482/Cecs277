"""


"""
import random as rand

from door import Door


class ComboDoor(Door):
    def __init__(self):
        self._correct_code = rand.randint(1,10)
        self._input = 0
    def examine_door(self):
        return "A door with a combination lock. You can spin the dial to a number 1-10."
    def menu_options(self):
        return "Enter # 1-10"

    def get_menu_max(self):
        options = 10
        return options
    
    def attempts(self, option):
        self._input = option
        print(f"You dialed to... {self._input}.")
        if self._input < self._correct_code:
            self.clue()
        if self._input > self._correct_code:
            self.clue()
        if self._correct_code == self._input:
            self._unlocked = True

    def is_unlocked(self):
        pass

    def clue(self):
        return "Too high" or "Too low"

    def success(self):
        return "You found the correct value and opened the door"

    