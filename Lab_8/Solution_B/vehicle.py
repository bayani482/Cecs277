import abc
import random as rand


class Vehicle(abc.ABC):
    def __init__(self, name, initial, speed):
        self.name = name
        self._initial = initial
        self._position = 0
        self._speed = speed
        self._energy = 100

    @property
    def initial(self):
        return self._initial
    
    @property
    def position(self):
        return self._position

    @property
    def energy(self):
        return self._energy
    
    def fast(self, obs_loc):
        if self._energy >= 5:
            self._energy -= 5
            move = rand.randint(-1,1)
        else:
            move = 1
        if obs_loc < self._position + self._speed:
            self._position += self.speed
            return f"{self._name} moved fast!"
        elif obs_loc >= self.position:
            self._position = obs_loc
            return f"{self._name} crashed into an obstacle."

    def slow(self, obs_loc):
        move = int(self._speed/2) + rand.randint(-1,1)
        if obs_loc < self._position + move:
            self._position += move
            return f"{self._name} moved slowly."
        elif obs_loc >= self._position:
            self._position += move
            return f"{self._name} moved slowly around obstacle."
        
    def __str__(self):
        return f"{self._name} [Position: -{self._position}, Energy - {self._energy}]"
    
    @abc.abstractmethod
    def special_move(self, obs_loc):
        pass