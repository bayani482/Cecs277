from door import Door
import random as rand

class LockedDoor(Door):
    def __init__(self):
        self.key_location = rand.randint(1,3)
        self._input = 0

    def examine_door(self):
        return "A locked door. The key is hidden nearby. Look around for the key."

    def menu_options(self):
        return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock."

    def get_menu_max(self):
        return 3

    def attempt(self, option):
        self._input = option
        match self._input:
            case 1:
                return "You look under the mat."
            case 2:
                return "You look under the flower pot."
            case 3:
                return "You look under the fake rock"

    def is_unlocked(self):
        if self._input == self.key_location:
            return True
        else:
            return False
    def clue(self):
        return "Look somewhere else."

    def success(self):
        return "Congratulations! You opened the locked door!"