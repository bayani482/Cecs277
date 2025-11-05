from entity import Entity
import random as rand

class Hero(Entity):
    def __init__(self, name):
        self._name = name
        self._hp = 25
    
    def melee_attack(self, enemy):
        damage = rand.randint(2,6)
        enemy.take_damage(damage)
        return f"{self._name} slashes a {enemy._name} with a sword for {damage} damage!"

    def ranged_attack(self, enemy):
        damage = rand.randint(1,12)
        enemy.take_damage(damage)
        return f"{self._name} pierces {enemy._name} with an arrow for {damage} damage!"
    