"""
basic_door class

"""
import random as rand

from door import Door


class BasicDoor(Door):
    def __init__(self):
        self._input = 0
        self._state = rand.randint(1,2)
    def examine_door(self):
        return "You encounter a basic door, you can either push it or pull it to open."

    def menu_options(self):
        return "1. Push\n2. Pull"

    def get_menu_max(self):
        options = 2
        return options
    
    def attempts(self, option):
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
        if self._input == self._state:
            return True
        else:
            return False

    def clue(self):
        return "Try the other way."

    def success(self):
        return "Congratulations, You opened the basic door."

