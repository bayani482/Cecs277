import random as rand

from vehicle import Vehicle

class Truck(Vehicle):
    def special_move(self,obs_loc):
        if self._energy >= 15:
            self._energy -= 15
            move = int(self._speed * 2)
            self._position += move

            movement = f"{self._name}  Ram forward {move} units."
        else:
            move = 1
            self._position += move
            movement = f"{self._name} tries to ram forward but, is all out of energy and moved {move} unit."

        return movement
