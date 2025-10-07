import random as rand

from dragon import Dragon


class FireDragon(Dragon):
    def __init__(self, name, max_hp,f_shots =3):
        super().__init__(name, max_hp)
        self.f_shots = f_shots
    def special_attack(self, hero):
        if self.swoops > 0:
            self.f_shots -= 1
            dmg = rand.randint(6,9)
            hero.take_damage(dmg)
            return f"{self.name} engulfs you in flames for {dmg} damage.\n"
        else:
            return f"{self.name} cant shoot fire anymore,you take 0 damage.\n"
    def __str__(self):
        return super().__str__() + f"\nFire Shots: {self.f_shots} remaining"