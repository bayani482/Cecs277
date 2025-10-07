import random as rand

from entity import Entity


class Hero(Entity):
    def sword_attack(self, dragon):
        dmg = rand.randint(1,6)+rand.randint(1,6)
        dragon.take_damage(dmg)
        return f"You slash the {dragon.name} with a sword for {dmg} damage."
    def arrow_attack(self, dragon):
        dmg = rand.randint(1,12)
        dragon.take_damage(dmg)
        return f"You hit {dragon.name} with a arrow for {dmg} damage."