"""
hero class
this class is a derived class from entity

Returns:
    str: returns a string of the attack performed and the damage done to the dragon 
"""

import random as rand

from entity import Entity
from map import Map


class Hero(Entity):
    def __init__(self, _name):
        """
        creates a hero entity with a location and map object.

        Args:
            Entity (object): a entity object
        attributes:
            _loc: tuple with ints
            _map: map object
        """
        self._loc = [0,0]
        self._map = Map()
        super().__init__(_name, 25)

    def attack(self, entity):
        """
        hero attacks dragon with a sword
        Args:
            dragon (object): the object the hero will attack
        Methods:
            take_damage(dmg): reduces the hp of the dragon by dmg and returns the current hp
        Returns:
            str: a string of the attack performed and the damage done to the dragon
        """
        dmg = rand.randint(2,5)
        entity.take_damage(dmg)
        return f"{self.name} attacks a {entity.name} for {dmg} damage."

    @property
    def loc(self):
        """getter for hero location

        Returns:
            int: tuple of location
        """
        return self._loc

    def go_north(self):
        """move hero location up

        Returns:
            char: tile value in the map
        """
        row = self._loc[0] -1
        if row >= 0:
            self._loc[0] = row
            return self._map.reveal(self._loc)
        else:
            return 'o'

    def go_south(self):
        """move hero location down

        Returns:
            char: tile value in the map
        """
        row = self._loc[0] + 1
        if row < len(self._map):
            self._loc[0] = row
            return self._map.reveal(self._loc)
        else:
            return 'o'

    def go_east(self):
        """move hero location right

        Returns:
            char: tile value in the map
        """
        col = self._loc[1] + 1
        if col < len(self._map[0]):
            self._loc[1] = col
            return self._map.reveal(self._loc)
        else:
            return 'o'

    def go_west(self):
        """move hero location left

        Returns:
            char: tile value in the map
        """
        col = self._loc[1] - 1
        if col >= 0:
            self._loc[1] = col
            return self._map.reveal(self._loc)
        else:
            return 'o'