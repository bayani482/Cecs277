"""
Hero Class
"""
import random as rand

from entity import Entity


class Hero(Entity):
    def __init__(self, name ):
        super().__init__(name, 25)
        

    def melee_attack(self, enemy):
        """
        Performs a melee attack on another entity.
        Args:
            enemy (Entity): the entity to attack
        Returns:
            str: attack description
        """
        dmg = (rand.randint(1,6)+ rand.randint(1,6))
        enemy._hp= enemy._hp - dmg
        return f"{self._name} slashes {enemy._name} for {dmg} damage."
    def ranged_attack(self, enemy):
        """
        Performs a ranged attack on another entity.
        Args:
            enemy (Entity): the entity to attack
        Returns:
            str: attack description
        """
        dmg = rand.randint(1,12)
        enemy._hp = enemy._hp - dmg
        return f"{self._name} pierces a {enemy._name} with an arrow for {dmg} damage."