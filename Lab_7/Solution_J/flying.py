from dragon import Dragon
import random as rand

class FlyingDragon(Dragon):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)
        self._swoop_attacks = 3

    def special_attack(self, hero):
        if self._swoop_attacks > 0:
            self._swoop_attacks -= 1
            dmg = rand.randint(5,8)
            hero.take_damage(dmg)
            return f"{self._name} swoops at you for {dmg} damage!"
        else:
            return f"{self._name} tries to swoop at you, but failed"
    def __str__(self):
        return super().__str__() + f"\nSwoops remaining: {self._swoop_attacks}"