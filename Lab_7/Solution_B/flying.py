import random as rand

from dragon import Dragon


class FlyingDragon(Dragon):
    def __init__(self, name, max_hp, swoops=3 ):
        super().__init__(name, max_hp)
        self.swoops = swoops
    def special_attack(self, hero):
        if self.swoops > 0:
            self.swoops -= 1
            dmg = rand.randint(5,8)
            hero.take_damage(dmg)
            return f"{self.name} swoops down and hits you for {dmg} damage.\n"
    def __str__(self):
        return super().__str__() + f"\nSwoops: {self.swoops} remaining"