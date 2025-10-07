"""
flying dragon class
this class is a subclass of dragon

Returns:
        __str__: returns a string of how many special attacks are left
"""

import random as rand

from dragon import Dragon


class FlyingDragon(Dragon):
    def __init__(self, name, max_hp, swoops=3 ):
        """
        initializes the flying dragon with a name, max hp, and number of swoops
        Args:
            name (_type_): _description_
            max_hp (_type_): _description_
            f_shots (int, optional): _description_. Defaults to 3.
        """
        super().__init__(name, max_hp)
        self.swoops = swoops
    def special_attack(self, hero):
        """
        dragon attacks hero with a special attack (fire shot) if it the swoop count is less than 0 it does 0 damage
        Args:
            hero (object): the object the dragon will attack
        Methods:
            take_damage(dmg): reduces the hp of the dragon by dmg and returns the current hp
        Returns:
            str: a string of the attack performed and the damage done to the hero
        """
        if self.swoops > 0:
            self.swoops -= 1
            dmg = rand.randint(5,8)
            hero.take_damage(dmg)
            return f"{self.name} swoops down and hits you for {dmg} damage.\n"
        else:
            return f"{self.name} cant swoop down anymore,you take 0 damage.\n"
    def __str__(self):
        return super().__str__() + f"\nSwoops: {self.swoops} remaining"