import random as rand
from vehicle import Vehicle

class Truck(Vehicle):
    """Truck: heavy and powerful; special is Ram (2x speed, costs energy)."""
    def special_move(self, obs_loc):
        """Ram forward: consumes 15 energy if available and moves ~2x speed.
        Ram lets truck ignore obstacles - it doesn't stop at them."""
        if self._energy >= 15:
            self._energy -= 15
            move = int(self._speed * 2) + rand.randint(-1, 1)
            if move < 1:
                move = 1
        else:
            move = 1
        self._position += move
        if obs_loc < self._position:
            return f"{self._name} rams through the obstacle and moves {move} units."
        return f"{self._name} rams forward and moves {move} units."