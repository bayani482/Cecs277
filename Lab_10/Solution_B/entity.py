"""
entity class
this class is a base class for hero and enemy

Returns:
    str: returns a string representation of the entity in the format "name: hp/max_hp"
"""

import abc


class Entity:
    """creates an entity with a name and hp
    attributes:
        _name: the name of the entity
        _hp: the current hp of the entity
        _max_hp: the maximum hp of the entity
    methods:
        name: returns the name of the entity
        hp: returns the current hp of the entity
        take_damage(dmg): reduces the hp of the entity by dmg and returns the current hp
        __str__: returns a string representation of the entity in the format "name: hp/max_hp"
    """
    def __init__(self, _name, _max_hp):
        """initializes the entity with a name and max hp

        Args:
            _name (str): name of the entity
            _hp (int): int value of the current hp of the entity
            _max_hp (int): int value of the maximum hp of the entity
            
        """
        self._name = _name
        self._hp = _max_hp
        self._max_hp = _max_hp
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
    def take_damage(self, dmg):
        """takes damage and reduces the hp of the entity by dmg

        Args:
            dmg (int): amount of damage to take

        Returns:
            int: left hp of the entity after taking damage, returns 0 if hp is less than 0
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
        return self._hp
    def heal(self):
        self._hp = self._max_hp
    @abc.abstractmethod
    def attack(self, entity):
        pass
    def __str__(self):
        """
        returns a string representation of the entity in the format "name: hp/max_hp
        """
        return f"{self._name}\nHP:{self._hp}/{self._max_hp}"