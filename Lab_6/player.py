"""
LAB 6
player class

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This class creates a player object that has a list of 3 dices rolls and initials points to keep track of the score
"""
from die import Die


class Player:
    
    def __init__(self):
        """
        Initializes a Player object with three dice and zero points.
        
        """
        self._dice = [Die(), Die(),Die()]
        self._dice.sort()
        self._points = 0

    @property
    def points(self):
        """
        Returns the player's current points.
        Returns:
            int: The player's current points.
        """
        return self
    
    def roll_dice(self):
        """
        rolls three dice and sorts them in ascending order.
        
        Returns:
            list: list of 3 dice rolls
        """
        for d in self._dice:
            d.roll()
        self._dice.sort()
        return self._dice
    def has_pair(self):
        """
        checks dice list to see if there is a pair if so adds 1 point to the players score

        Returns:
            bool: True if there is a pair, False otherwise.
        """
        for i in range(len(self._dice)):
            if self._dice[i] == self._dice[i-1]:
                self._points += 1
                return True
        return False
    def has_three_of_a_kind(self):
        """
        checks dice list to see if there is a three of a kind if so adds 3 point to the players score

        Returns:
            bool: True if there is a pair, False otherwise.
        """
        if self._dice[0] == self._dice[1] == self._dice[2]:
            self._points += 3
            return True
        else:
            return False
    def has_series(self):
        """
        checks dice list to see if there is a series if so adds 2 point to the players score

        Returns:
            bool: True if there is a pair, False otherwise.
        """
        if self._dice[1] - self._dice[0] == 1 and self._dice[2] - self._dice[1] == 1:
            self._points += 2
            return True
        else:
            return False        # Use Die's __sub__ to check for sequence
    def __str__(self):
        """
        changes the player object to a string representation of the dice rolls

        Returns:
            str: formatted string of the dice rolls
        """
        return f"D1={self._dice[0]._value}, D2={self._dice[1]._value}, D3={self._dice[2]._value}"

