from entity import Entity
import random as rand

class ExpTroll(Entity):
    def __init__(self):
        super().__init__("Experienced Troll", rand.randint(15,18))

    def melee_attack(self, enemy):
        damage = rand.randint(8,12)
        enemy.take_damage(damage)
        return f"{self._name} crushes {enemy._name} for {damage} damage!"