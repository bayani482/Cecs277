from door import Door
import random as rand

""" Basic Door Class for Escape Room Game
    Inherits from Door superclass.
    The door can be opened by either pushing or pulling it.
"""
class BasicDoor(Door):
    def __init__(self):
        self._state = rand.randint(1,2)
        self._input = 0

    def examine_door(self):
        """Examines the basic door.
        Returns:
            str: Description of the basic door.
        """
        return "You encounter a basic door, you can either push it or pull it to open."
    
    def menu_options(self):
        """Provides menu options for the basic door.
        Returns:
            str: Menu options for the basic door."""
        return "1. Push\n2. Pull"
    
    def get_menu_max(self):
        """Gets the maximum menu option number.
        Returns:
            int: Maximum menu option number.
        """
        return 2
    
    def attempt(self,option):   
        """Attempts to open the door based on user input.
        Args:
            option (int): User's choice to push or pull the door.
        Returns:
            str: Result of the attempt to open the door.
        """
        self._input = option
        match self._input:
            case 1:
                return "You push the door."
            case 2:
                return "You pull the door."
            
    def is_unlocked(self):
        """Checks if the door is unlocked based on user input.
        Returns:
            bool: True if the door is unlocked, False otherwise.
        """
        if self._input == self._state:
            return True
        else:
            return False
        
    def clue(self):
        """Provides a clue if the door is not opened.
        Returns:
            str: Clue message.
        """
        return "Try the other way."
    
    def success(self):
        """Provides success message when the door is opened.
        Returns:
            str: Success message.
        """
        return "Congratulations, you opened the door."
    

