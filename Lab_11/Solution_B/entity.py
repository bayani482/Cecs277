"""

Entity class
"""
import abc


class Entity:
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        
    @property
    def name(self):
        """gets the name of the entity

        Returns:
            str: name of the entity
        """
        return self._name

    @property
    def hp(self):
        """gets the current hp of the entity

        Returns:
            int: hp of the entity
        """
        return self._hp

    def __str__(self):
        return f"Name: {self.name}, Health: {self._hp})"
    
    @abc.abstractmethod
    def melee_attack(self, enemy):
        """performs a melee attack on another entity

        Args:
            other (Entity): the entity to attack
        """
        pass