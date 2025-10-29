from entity import Entity
from map import Map
import random as rand

class Hero(Entity):
    def __init__(self, name):
        self._max_hp = 25
        self._hp = self._max_hp
        self._name = name
        self._loc = [0, 0]
        self._map = Map()  # Store map reference once

    @property
    def loc(self):
        return self._loc
    
    def attack(self, entity):
        damage = rand.randint(2,5)
        entity.take_damage(damage)
        print(f"{self._name} attacks {entity._name} for {damage} damage!")

    def go_north(self):
        new_row = self._loc[0] - 1  # North decreases row
        if new_row >= 0:  # Check boundary
            self._loc[0] = new_row
            return self._map.reveal(self._loc)
        else:
            return 'o'  # Out of bounds

    def go_south(self):
        new_row = self._loc[0] + 1  # South increases row
        if new_row < len(self._map):  # Check boundary
            self._loc[0] = new_row
            return self._map.reveal(self._loc)
        else:
            return 'o'  # Out of bounds

    def go_east(self):
        new_col = self._loc[1] + 1  # East increases column
        if new_col < len(self._map[0]):  # Check boundary
            self._loc[1] = new_col
            return self._map.reveal(self._loc)
        else:
            return 'o'  # Out of bounds

    def go_west(self):
        new_col = self._loc[1] - 1  # West decreases column
        if new_col >= 0:  # Check boundary
            self._loc[1] = new_col
            return self._map.reveal(self._loc)
        else:
            return 'o'  # Out of bounds

    def __str__(self):
        return f"{self.name}\n{self._hp}/{self._max_hp}"
    


