"""
Beginner Troll Enemy Class

"""

import random as rand

from entity import Entity


class BegTroll(Entity):
    def __init__(self):
        super().__init__("Beginner Troll",rand.randint(8,10) )
    
    def melee_attack(self, enemy):
        """
        Performs a melee attack on another entity.
        Args:
            enemy (Entity): the entity to attack

        Returns:
            str: attack description
        """
        dmg = (rand.randint(5,9))
        enemy.take_damage(dmg)
        return f"{self._name} slashes {enemy._name} for {dmg} damage."
        