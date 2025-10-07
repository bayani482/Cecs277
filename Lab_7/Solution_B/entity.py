
class Entity:
    def __init__(self, _name, _max_hp):
        self._name = _name
        self._hp = _max_hp
        self._max_hp = _max_hp
    
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
        return self._hp
    def __str__(self):
        return f"{self._name}:{self._hp}/{self._max_hp}"