from door import Door
import random as rand   

""" Combo Door Class for Escape Room Game
    Inherits from Door superclass.
    The door has a combination lock with a number between 1 and 10."""

class ComboDoor(Door):
    def __init__(self):
        self._correct_value = rand.randint(1,10)
        self._input = 0
    
    def examine_door(self):
        """Examines the combo door.
        Returns:
            str: Description of the combo door.
        """
        return "A door with a combination lock. You can spin the dial to a number 1-10."
    
    def menu_options(self):
        """Provides menu options for the combo door.
        Returns:
            str: Menu options for the combo door.
        """
        return "Enter # 1-10:"
    
    def get_menu_max(self):
        """Gets the maximum menu option number.
        Returns:
            int: Maximum menu option number."""
        return 10
    
    def attempt(self,option):
        """Attempts to open the door based on user input.
        Args:
            option (int): User's chosen number for the combination lock.
        Returns:
            str: Result of the attempt to open the door.
        """
        self._input = option
        return f"You spin the dial to {self._input}."
    
    def is_unlocked(self):
        """Checks if the door is unlocked based on user input.
        Returns:
            bool: True if the door is unlocked, False otherwise.
        """
        if self._input == self._correct_value:
            return True
        else:
            return False
        
    def clue(self):
        """Provides a clue if the door is not opened.
        Returns:
            str: Clue message."""
        if self._input < self._correct_value:
            return "Too low."
        else:
            return "Too high."
        
    def success(self):
        """Provides a success message if the door is opened.
        Returns:
            str: Success message.
        """
        return "Congratulations! You opened the combo lock door."