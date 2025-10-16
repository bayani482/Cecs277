import random as rand

from vehicle import Vehicle


class Motorcycle(Vehicle):
    def slow(self, obs_loc):
            move = int(self._speed * 0.75) + rand.randint(-1, 1)
            move = max(1, move)
            
            if obs_loc is None:
                self._position += move
                if self._position > 100:
                    self._position = 100
                return f"{self._name} moves slowly {move} units."
            
            if move >= obs_loc:
                self._position += move
                if self._position > 100:
                    self._position = 100
                return f"{self._name} slowly dodges the obstacle and moves {move} units."
            else:
                self._position += move
                return  f"{self._name} moves slowly {move} units."


    def special_move(self, obs_loc):
        if self._energy < 15:
            self._position += 1
            return f"{self._name} doesn't have enough energy for a wheelie and only moves 1 unit."

        self._energy -= 15
        if rand.random() <= 0.75:#wheelie chance
            move = int(self._speed * 2) + rand.randint(-1, 1)
            move = max(1,move)
            if obs_loc is None:# no obstacle
                self._position += move
                return f"{self._name} does a wheelie and moves {move} units!"
            if move >= obs_loc:# there is an obstacle
                self._position += move
                return f"{self._name} tries a wheelie, moves {move} unit(s) and crashes into an obstacle!"
            else:
                self._position += move# gets the 75% chance boost
                return f"{self._name} does a wheelie and moves {move} units!"
        else:#wheelie chance fail
            self._position += 1
            return f"{self._name} doesn't have enough energy for a wheelie and only moves 1 unit."
