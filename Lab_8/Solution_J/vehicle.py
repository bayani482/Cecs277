import abc
import random as rand

class Vehicle(abc.ABC):
    """Abstract base for vehicles.

    Public API used by main.py:
      - get_speed() -> int
      - get_energy() -> int
      - get_position() -> int
      - get_initial() -> str
      - fast(obs_loc), slow(obs_loc), special_move(obs_loc) -> str
      - __str__() for status display
    """
    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._position = 0
        self._speed = int(speed)
        self._energy = 100

    def get_speed(self):
        """Return base speed."""
        return self._speed

    def get_energy(self):
        """Return remaining energy."""
        return self._energy

    def get_position(self):
        """Public getter for current position."""
        return self._position

    def get_initial(self):
        """Public getter for the vehicle initial."""
        return self._initial

    def set_initial(self, new_initial):
        """Public setter for the vehicle initial."""
        self._initial = new_initial

    def fast(self, obs_loc):
        """Fast move: consumes small energy, advances; stops at obstacle if within range."""
        move = 1  # Default move if not enough energy
        
        if self._energy >= 5:
            self._energy -= 5
            move = int(self._speed) + rand.randint(-1, 1)

        new_pos = self._position + move
        if obs_loc < new_pos:
            self._position = obs_loc
            return f"{self._name} CRASHED into an obstacle!"
            
        self._position = new_pos
        return f"{self._name} quickly moves {move} units."

    def slow(self, obs_loc):
        """Slow move: controlled advance; if an obstacle is in the move range,
        go around it by moving to obs_loc + 1."""
        old_pos = self._position
        move = int(self._speed / 2) + rand.randint(-1, 1)
        if move < 1:
            move = 1
            
        if obs_loc < (old_pos + move):
            self._position = obs_loc + 1
            moved = self._position - old_pos
            return f"{self._name} dodges the obstacle and moves {moved} units."
        
        self._position += move
        return f"{self._name} slowly moves {move} units."

    def __str__(self):
        return f"{self._name} [Position: {self._position}, Energy: {self._energy}]"

    @abc.abstractmethod
    def special_move(self, obs_loc):
        pass