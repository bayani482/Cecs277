"""
LAB 5
die class

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This class Creates a Die object with 6 sides that can be rolled and compare 2 other dices to see if
they are equal, less than, or add them together.
"""

import random


class Die:
    """
    Represents a single Die. Defaults to a 6-sided die.
    Attributes:
    sides (int): Number of sides on the die.
    _value (int): The _value of the rolled die.
    """
    def __init__(self, _sides=6):
        """
        Initializes a Die object.
        Args:
        sides (int): The number of sides on the die. Defaults to 6.
        """
        self._sides = _sides
        self._value = self.roll()
    def roll(self):
        """
        Rolls the die to set and return a random _value.
        Returns:
        int: The randomly generated _value between 1 and `sides`.
        """
        self._value = random.randint(1, self._sides)
        return self._value
    def __str__(self):
        """
        Returns the string representation of the die.
        Returns:
        str: The string form of the die's _value.
        """
        return str(self._value)
    def __add__(self, other):
        """
        Adds the _values of two dice.
        Args:
        other (Die): Another die object.
        Returns:
        int: The sum of self._value and other._value.
        """
        return self._value + other._value
    def __lt__(self, other):
        """
        Compares if this die's _value is less than another die's _value.
        Args:
        other (Die): Another die object.
        Returns:
        bool: True if self._value < other._value, otherwise False.
        """
        return self._value < other._value
    def __eq__(self, other):
        """
        Compares if this die's _value is equal to another die's _value.
        Args:
        other (Die): Another die object.
        Returns:
        bool: True if self._value == other._value, otherwise False.
        """
        return self._value == other._value
    def __sub__(self,other):
        """
        subtracts the _values of two dice.
        Args:
        other (Die): Another die object.
        Returns:
        int: The difference of self._value and other._value.
        """
        return self._value - other._value