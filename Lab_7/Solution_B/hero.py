"""
hero class
this class is a derived class from entity

Returns:
    str: returns a string of the attack performed and the damage done to the dragon 
"""

import random as rand

from entity import Entity


class Hero(Entity):
    """
    creates a hero with a name and hp.

    Args:
        Entity (_type_): _description_
    attributes:
        _name: the name of the hero
        dragon: the dragon the hero is fighting

    """
    def sword_attack(self, dragon):
        """
        hero attacks dragon with a sword
        Args:
            dragon (object): the object the hero will attack
        Methods:
            take_damage(dmg): reduces the hp of the dragon by dmg and returns the current hp
        Returns:
            str: a string of the attack performed and the damage done to the dragon
        """
        dmg = rand.randint(1,6)+rand.randint(1,6)
        dragon.take_damage(dmg)
        return f"You slash the {dragon.name} with a sword for {dmg} damage."
    def arrow_attack(self, dragon):
        """
        hero attacks dragon with a sword
        Args:
            dragon (object): the object the hero will attack
        Methods:
            take_damage(dmg): reduces the hp of the dragon by dmg and returns the current hp
        Returns:
            str: a string of the attack performed and the damage done to the dragon
        """
        dmg = rand.randint(1,12)
        dragon.take_damage(dmg)
        return f"You hit {dragon.name} with a arrow for {dmg} damage."