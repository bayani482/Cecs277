"""

"""
import random as rand

#hero class extends from entity class
import entity


class Hero(entity):
    def __init__(self, name, hp):
        super().__init__(name, hp)
    @property

    def melee_attack(self, enemy):
        """performs a melee attack on another entity

        Args:
            enemy (Entity): the entity to attack
        """
        dmg = (rand.randint(1,6)+ rand.randint(1,6))
        enemy._hp= enemy._hp - dmg
        return f"{self._name} slashes {enemy._name} for {dmg} damage."
    def ranged_attack(self, enemy):
        """performs a ranged attack on another entity

        Args:
            enemy (Entity): the entity to attack
        """
        dmg = rand.randint(1,12)
        enemy._hp= enemy._hp - dmg
        return f"{self._name} pierces a {enemy._name} with an arrow for {dmg} damage."