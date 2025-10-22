from door import Door
import random as rand

""" Locked Door Class for Escape Room Game
    Inherits from Door superclass.
    The door is locked and the key is hidden in one of three locations."""

class LockedDoor(Door):
    def __init__(self):
        self.key_location = rand.randint(1,3)
        self._input = 0

    def examine_door(self):
        """Examines the locked door.
        Returns:
            str: Description of the locked door."""
        return "A locked door. The key is hidden nearby. Look around for the key."

    def menu_options(self):
        """Provides menu options for the locked door.
        Returns:
            str: Menu options for the locked door.
        """
        return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock."

    def get_menu_max(self):
        """Gets the maximum menu option number.
        Returns:
            int: Maximum menu option number.
        """
        return 3

    def attempt(self, option):
        """Attempts to open the door based on user input.
        Args:
            option (int): User's chosen location to look for the key.
        Returns:
            str: Result of the attempt to find the key.
        """
        self._input = option
        match self._input:
            case 1:
                return "You look under the mat."
            case 2:
                return "You look under the flower pot."
            case 3:
                return "You look under the fake rock"

    def is_unlocked(self):
        """Checks if the door is unlocked based on user input.
        Returns:
            bool: True if the door is unlocked, False otherwise."""
        if self._input == self.key_location:
            return True
        else:
            return False
        
    def clue(self):
        """Provides a clue if the door is not opened.
        Returns:
            str: Clue message."""
        return "Look somewhere else."

    def success(self):
        """Provides a success message if the door is opened.
        Returns:
            str: Success message.
        """
        return "Congratulations! You opened the locked door!"