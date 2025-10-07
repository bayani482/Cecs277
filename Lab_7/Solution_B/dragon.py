

import random as rand

from entity import Entity


class Dragon(Entity):
    def basic_attack(self, hero):
        dmg = rand.randint(2,5)
        hero.take_damage(dmg)
        return f"{self.name} smashes you with its tail for {dmg} damage.\n"
    def special_attack(self, hero):
        dmg = rand.randint(3,7)
        hero.take_damage(dmg)
        return f"{self.name} slashes you with its claw for {dmg} damage.\n"