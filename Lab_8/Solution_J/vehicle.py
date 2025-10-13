import abc
import random as rand

class Vehicle(abc.ABC):
    def __init__(self,name,initial,speed):
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
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
    
    def fast(self,obs_loc):
        if self._energy >= 5:
            self._speed += rand.randint(-1,1)
            self._energy -= 5
            if self._speed < obs_loc:
                self._position += self._speed
            else:
                self._position = obs_loc
                return f"{self._name} CRASHED into an obstacle!"
        else:
            self._position += 1
            return f"{self._name} tries to speed forward, but it's all out of energy! 1 unit moved"
        return f"{self._name} quickly moves {self._position} units forward!"
    
    def slow(self,obs_loc):
        self._speed = int(self._speed*0.5 + rand.randint(-1,1))
        self._position += self._speed
        if self._position == obs_loc:
            self._position += 1
            return f"{self._name} slows down and goes around an obstacle! Moving {self._position} units forward!"
        return f"{self._name} slowly moves {self.position} units forward!"


    @abc.abstractmethod
    def special_move(self,obs_loc):
        pass
    
    def __str__(self):
        return f"Name: {self._name}\nPosition: {self._position}\nEnergy: {self._energy}\nSpeed: {self._speed}"