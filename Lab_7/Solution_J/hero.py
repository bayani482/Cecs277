import random as rand

from entity import Entity

class Hero(Entity):
    def sword_attack(self,dragon):
        dmg = rand.randint(2,6)
        dragon.take_damage(dmg)
        return f"You slash the {dragon._name} with your sword for {dmg} damage."

    def arrow_attack(self,dragon):
        dmg = rand.randint(1,12)
        dragon.take_damage(dmg)
        return f"You hit the {dragon._name} with an arrow for {dmg} damage."