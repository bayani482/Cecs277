

from vehicle import Vehicle


class Truck(Vehicle):
    def special_move(self,obs_loc):
        if self._energy >= 15:
            self._energy -= 15
            move = int(self._speed * 2)
            self._position += move
            return f"{self._name} Ram forward {move} units."
        else:
            self._position += 1
            return f"{self._name} tries to ram forward but, is all out of energy and moved 1 unit."

