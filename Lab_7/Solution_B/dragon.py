"""
dragon class
this class is a derived class from entity

Returns:
    str: returns a string of the attack performed and the damage done to the hero
"""

import random as rand

from entity import Entity


class Dragon(Entity):
    def basic_attack(self, hero):
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
    def special_attack(self, hero):
        """
        Dragon attacks hero with its claw
        Args:
            hero (object): the object the dragon will attack
        Methods:
            take_damage(dmg): reduces the hp of the dragon by dmg and returns the current hp
        Returns:
            str: a string of the attack performed and the damage done to the hero
        """
        dmg = rand.randint(3,7)
        hero.take_damage(dmg)
        return f"{self.name} slashes you with its claw for {dmg} damage.\n"