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
        """
        String representation of the entity
        Returns:
            str: string representation
        """
        return f"Name: {self.name} Hp: {self._hp}"
    
    @abc.abstractmethod
    def melee_attack(self, enemy):
        """
        Performs a melee attack on another entity.

        Args:
            other (Entity): the entity to attack
        """
        pass
    
    def take_damage(self, dmg):
        """
        Reduces the entity's hp by the damage taken. and if its less than 0 sets it to 0
        Args:
            dmg (int): the amount of damage taken
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0