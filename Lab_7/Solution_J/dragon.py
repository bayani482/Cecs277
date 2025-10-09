import random as rand

from entity import Entity

class Dragon(Entity):
    """
    creates a dragon entity with a name and hp.

    Args:
        Entity (object): a entity object
    attributes:
        _name: the name of the dragon
        _hp: the current hp of the dragon
    """
    def basic_attack(self,hero):
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
        return f"{self._name} smashes you with its tail for {dmg} damage points!"

    def special_attack(self,hero):
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
        return f"{self._name} slashes you with its claws for {dmg} damage points!"