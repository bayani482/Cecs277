from entity import Entity
import random as rand

class ExpGoblin(Entity):
    def __init__(self):
        super().__init__("Experienced Goblin", rand.randint(12,15))

    def melee_attack(self, enemy):
        damage = rand.randint(5,8)
        enemy.take_damage(damage)
        return f"{self._name} slams {enemy._name} for {damage} damage!"
    
