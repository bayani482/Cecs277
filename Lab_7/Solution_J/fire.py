from dragon import Dragon
import random as rand

class FireDragon(Dragon):
    def __init__(self, name, max_hp):
        super().__init__(name, max_hp)
        self._fire_shots = 2

    def special_attack(self, hero):
        # if there are shots left, perform attack and decrement
        if self._fire_shots > 0:
            dmg = rand.randint(6,9)
            hero.take_damage(dmg)
            self._fire_shots -= 1
            return f"{self._name} engulfs you in flames for {dmg} damage!"
        # if exactly 0, set to -1 (allow one failing attempt to move to -1)
        else:
            return f"{self._name} tries to spit fire at you, but failed"
        
    def __str__(self):
        return super().__str__() + f"\nFire shots remaining: {self._fire_shots}"