from entity import Entity
import random as rand

class Enemy(Entity):

    def __init__(self):
        names = ["Goblin","Vampire","Ghoul","Skeleton","Zombie"]
        self._name = rand.choice(names)
        self._max_hp = rand.randint(4,8)
        self._hp = self._max_hp

    def attack(self,entity):
        damage = rand.randint(1,4)
        entity.take_damage(damage)
        print(f"{self._name} attacks {entity._name} for {damage} damage!")