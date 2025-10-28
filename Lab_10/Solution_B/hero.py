"""
hero class
this class is a derived class from entity

Returns:
    str: returns a string of the attack performed and the damage done to the dragon 
"""

import random as rand

from entity import Entity


class Hero(Entity):
    def __init__(self, _name):
        self._row = 0
        self._col = 0
        super().__init__(_name, 25)
    """
    creates a hero entity with a name and hp.

    Args:
        Entity (object): a entity object
    attributes:
        _name: the name of the hero
        _hp: the current hp of the hero
    """
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
    def loc(self):
        return self._row,self._col
    def go_north(self, game_map):
        if self._row > 0 and game_map[self._row - 1][self._col] != 'o':
            self._row -= 1
        return game_map[self._row][self._col]

    def go_south(self, game_map):
        if self._row < len(game_map) - 1 and game_map[self._row + 1][self._col] != 'o':
            self._row += 1
        return game_map[self._row][self._col]

    def go_east(self, game_map):
        if self._col < len(game_map[0]) - 1 and game_map[self._row][self._col + 1] != 'o':
            self._col += 1
        return game_map[self._row][self._col]

    def go_west(self, game_map):
        if self._col > 0 and game_map[self._row][self._col - 1] != 'o':
            self._col -= 1
        return game_map[self._row][self._col]