import abc
import random as rand


class Vehicle(abc.ABC):
    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._position = 0
        self._speed = speed
        self._energy = 100

    @property
    def initial(self):
        return self._initial
    @property
    def name(self):
        return self._name
    @property
    def position(self):
        return self._position

    @property
    def energy(self):
        return self._energy
    
    @property
    def speed(self):
        return self._speed
    
    def fast(self, obs_loc):
        if self._energy >= 5:
            self._energy -= 5
            move = self._speed + rand.randint(-1,1)
        else:
            move = 1

        move = max(1, move)
        
        if obs_loc is None:
            if self._position > 100:
                self._position = 100
            return f"{self._name} quickly moves {self._speed} units."

        if move >= obs_loc:
            move = obs_loc
            self._position += move
            if self._position > 100:
                self._position = 100
            return f"{self._name} crashed into an obstacle."
        
        self._position += move
        return f"{self._name} quickly moves {self._speed} units."

    def slow(self, obs_loc):
        move = int(self._speed/2) + rand.randint(-1,1)
        move = max(1, move)
        
        if obs_loc is None:
            self._position += move
            if self._position > 100:
                self._position = 100
            return f"{self._name} slowly moves {move} units."
    
        if move >= obs_loc:
            self._position += move
            if self._position > 100:
                self._position = 100
            return f"{self._name} slowly moves around the obstacle {move} units."
        
        self._position += move
        return f"{self._name} slowly moves {move} units."

    def __str__(self):
        return f"{self._name} [Position: - {self._position}, Energy - {self._energy}]"
    
    @abc.abstractmethod
    def special_move(self, obs_loc):
        pass