import abc

class Entity(abc.ABC):
    def __init__(self,name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp

    @abc.abstractmethod
    def melee_attack(self,enemy):
        pass

    def __str__(self):
        return f"{self._name} HP: {self._hp}"
    
    def take_damage(self,dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
    