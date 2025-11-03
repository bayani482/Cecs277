"""


"""

import random as rand

from entity import Entity
from hero import hero

class BegGoblin(Entity):
    def __init__(self):
        super().__init__("Beginner Goblin",rand.randint(7,9) )
    
    def melee_attack(self, enemy):
        """performs a melee attack on another entity

        Args:
            enemy (Entity): the entity to attack
        """
        dmg = (rand.randint(4,6))
        hero._hp= enemy._hp - dmg
        return f"{self._name} slashes {hero._name} for {dmg} damage."
    