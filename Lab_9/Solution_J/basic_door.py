from door import Door

class BasicDoor(Door):
    def __init__(self):
        super().__init__()

    def examine_door(self):
        return "You encounter a basic door, you can either push it or pull it to open."
    
    def menu_options(self):
        return "1. Push\n2.Pull"
    
    def get_menu_max(self):
        return 2
    
    def attempt(self,option):
        match option:
            case 1:
                return "You push the door."
            case 2:
                return "You pull the door."
    def is_unlocked(self):
        return True
    
    def clue(self):
        return "Simply push or pull the door"
    
    def success(self):
        return "Congratulations, you opened the door."
    
    

