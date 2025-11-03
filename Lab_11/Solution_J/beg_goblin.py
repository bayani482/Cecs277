from entity import Entity
import random as rand

class BegGoblin(Entity):
    def __init__(self):
        super().__init__("Beg Goblin", rand.randint(7,9))

    def melee_attack(self, enemy):
        damage = rand.randint(4,6)
        enemy.take_damage(damage)
        return f"{self._name} bites {enemy._name} for {damage} damage!"