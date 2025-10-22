from door import Door
import random as rand

class DeadboltDoor(Door):
    def __init__(self):
        self._bolt1,self._bolt2 = rand.randint(0,1), rand.randint(0,1)  # 0 = locked, 1 = unlocked
        self._input = 0
    def examine_door(self):
        return """
A door with two deadbolts.
Both need to be unlocked to open the door,
but you can't tell if each one is locked or unlocked."""

    def menu_options(self):
        return "1. Toggle bolt 1\n2. Toggle bolt 2"
    
    def get_menu_max(self):
        return 2
    
    def attempt(self,option):
        self._input = option
        match self._input:
            case 1:
                self._bolt1 = 1 - self._bolt1
                return "You toggle the first bolt."
            case 2:
                self._bolt2 = 1 - self._bolt2
                return "You toggle the second bolt."

    def is_unlocked(self):
        if self._bolt1 == 1 and self._bolt2 == 1:
            return True
        else:
            return False
    
    def clue(self):
        if self._bolt1 == 1 and self._bolt2 == 0 or self._bolt1 == 0 and self._bolt2 == 1:
            return "You jiggle the door... it seems like one of the bolts is unlocked."
        else:
            return "...it seems like it's completely locked"
    
    def success(self):
        return "Congratulations! You unlocked both deadbolts and opened the door."
    