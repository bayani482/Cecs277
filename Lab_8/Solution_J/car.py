import random as rand
from vehicle import Vehicle

class Car(Vehicle):
    """Car: has Nitro Boost special (1.5x speed, costs energy)."""
    def special_move(self, obs_loc):
        """Nitro Boost: consumes 15 energy if available and moves ~1.5x speed."""
        move = 1
        if self._energy >= 15:
            self._energy -= 15
            move = max(1, int(self._speed * 1.5) + rand.randint(-1, 1))
        else:
            move = 1
        self._position += move
        if obs_loc <= self._position and obs_loc < obs_loc + 1:
            self._position = obs_loc
            return f"{self._name} CRASHED into an obstacle!"
        return f"{self._name} uses Nitro Boost and moves {move} units."
