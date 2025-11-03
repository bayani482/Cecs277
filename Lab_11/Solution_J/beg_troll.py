from entity import Entity
import random as rand

class BegTroll(Entity):
    def __init__(self):
        super().__init__("Begging Troll", rand.randint(8,10))

    def melee_attack(self, enemy):
        damage = rand.randint(5,9)
        enemy.take_damage(damage)
        return f"{self._name} slaps {enemy._name} for {damage} damage!"