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
        monster = rand.choice(names)
        names = ["Goblin","Vampire","Ghoul","Skeleton","Zombie"]
        
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
        dmg = rand.randint(2,5)
        hero.take_damage(dmg)
        return f"{self.name} smashes you with its tail for {dmg} damage.\n"