"""
expert goblin class

"""

import random as rand

from entity import Entity
from hero import hero


class ExpTroll(Entity):
    def __init__(self):
        super().__init__("Expert Troll",rand.randint(15,18) )
    
    def melee_attack(self, enemy):
        """performs a melee attack on another entity

        Args:
            enemy (Entity): the entity to attack
        """
        dmg = (rand.randint(8,12))
        hero._hp= enemy._hp - dmg
        return f"{self._name} slashes {hero._name} for {dmg} damage."
        