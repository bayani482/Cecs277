from door import Door
import random as rand

class BasicDoor(Door):
    def __init__(self):
        self._state = rand.randint(1,2)
        self._input = 0

    def examine_door(self):
        return "You encounter a basic door, you can either push it or pull it to open."
    
    def menu_options(self):
        return "1. Push\n2. Pull"
    
    def get_menu_max(self):
        return 2
    
    def attempt(self,option):   
        self._input = option
        match self._input:
            case 1:
                return "You push the door."
            case 2:
                return "You pull the door."
            
    def is_unlocked(self):
        if self._input == self._state:
            return True
        else:
            return False
        
    def clue(self):
        return "Try the other way."
    
    def success(self):
        return "Congratulations, you opened the door."
    

