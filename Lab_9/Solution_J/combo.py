from door import Door
import random as rand   

class ComboDoor(Door):
    def __init__(self):
        self._correct_value = rand.randint(1,10)
        self._input = 0
    
    def examine_door(self):
        return "A door with a combination lock. You can spin the dial to a number 1-10."
    
    def menu_options(self):
        return "Enter # 1-10:"
    
    def get_menu_max(self):
        return 10
    
    def attempt(self,option):
        self._input = option
        return f"You spin the dial to {self._input}."
    
    def is_unlocked(self):
        if self._input == self._correct_value:
            return True
        else:
            return False
        
    def clue(self):
        if self._input < self._correct_value:
            return "Too low."
        else:
            return "Too high."
    def success(self):
        return "Congratulations! You opened the combo lock door."