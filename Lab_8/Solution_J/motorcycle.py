import random as rand
from vehicle import Vehicle

class Motorcycle(Vehicle):
    """Motorcycle: fast and nimble; special is Wheelie (high risk/reward)."""
    def slow(self, obs_loc):
        """Motorcycle slow: smaller controlled move with better dodge handling."""
        move = max(1, int(self._speed * 0.75) + rand.randint(-1, 1))
        new_pos = self._position + move
        if obs_loc <= new_pos and obs_loc < obs_loc + 1:
            # treat as stopped by obstacle
            self._position = obs_loc
            return f"{self._name} CRASHES at an obstacle!"
        self._position = new_pos
        return f"{self._name} moves slowly {move} units."

    def special_move(self, obs_loc):
        """Wheelie: costs 15 energy; 75% chance to succeed and move 2x speed, else fall and move 1."""
        move = 1  # default value
        
        if self._energy >= 15:
            self._energy -= 15
            if rand.random() <= 0.75:
                move = int(self._speed * 2) + rand.randint(-1, 1)
                if move < 1:
                    move = 1
                self._position += move
                if obs_loc < self._position:
                    self._position = obs_loc
                    return f"{self._name} CRASHED into an obstacle!"
                return f"{self._name} pops a wheelie and moves {move} units!"
            else:
                self._position += move
                return f"{self._name} tried to do a wheelie but wiped out and only moves {move} unit!"
        
        self._position += move

        return f"{self._name} tried to do a wheelie but didn't have enough energy and moves {move} unit."
