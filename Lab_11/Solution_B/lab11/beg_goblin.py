"""
beg_goblin.py: Beginner Goblin Enemy Class

"""

import random as rand

from entity import Entity


class BegGoblin(Entity):
    def __init__(self):
        super().__init__("Beginner Goblin",rand.randint(7,9))
    
    def melee_attack(self, enemy):
        """
        Performs a melee attack on another entity.
        Args:
            enemy (Entity): the entity to attack

        Returns:
            str: attack description
        """
        dmg = (rand.randint(4,6))
        enemy.take_damage(dmg)
        return f"{self._name} slashes {enemy._name} for {dmg} damage."
