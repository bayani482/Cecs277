"""
enemy class
this class is a derived class from entity

Returns:
    str: returns a string of the attack performed and the damage done to the hero
"""

import random as rand

from entity import Entity


class Enemy(Entity):
    """
    creates a enemy entity with a name and hp.

    Args:
        Entity (object): a entity object
    attributes:
        _name: the name of the dragon
        _hp: the current hp of the dragon
    """
    def __init__(self):
        name = rand.choice(["Goblin","Vampire","Ghoul","Skeleton","Zombie"])
        hp = rand.randint(4,8)
        super().__init__(name,hp)
    def attack(self, hero):
        """
        dragon attacks hero with a tail smash
        Args:
            hero (object): the object the dragon will attack
        Methods:
            take_damage(dmg): reduces the hp of the dragon by dmg and returns the current hp
        Returns:
            str: a string of the attack performed and the damage done to the dragon
        """
        dmg = rand.randint(1,4)
        hero.take_damage(dmg)
        return f"{self.name} attacks {hero.name} for {dmg} damage.\n"