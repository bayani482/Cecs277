"""
deadbolt class

"""

import random as rand

from door import Door


class Deadbolt(Door):
    def __init__(self):
        self._bolt1 = rand.randint(1,2)
        self._bolt2 = rand.randint(1,2)
    def examine_door(self):
        return " You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked"

    def menu_options(self):
        return "1. Toggle bolt 1\n2. Toggle bolt 2"

    def get_menu_max(self):
        options = 2
        return options
    
    def attempts(self, option):
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
        if self._bolt1 == 1 and self._bolt2 == 1:
            return True
        else:
            return False

    def clue(self):
        if self._bolt1 == 2 and self._bolt2 == 2:
            return "You jiggle the door... it's completely locked."
        else: #(self._bolt1 == 1 and self._bolt2 == 2) or (self._bolt1 == 2 and self._bolt2 == 1)
            return "You jiggle the door... it seems like one of the bolts is unlocked."

    def success(self):
        return "You unlocked both deadbolts and opened the door"
    
    
