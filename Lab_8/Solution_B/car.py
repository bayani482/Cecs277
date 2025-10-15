
import random as rand

from vehicle import Vehicle


class Car(Vehicle):
    def special_move(self,obs_loc):
        if self._energy >= 15:
            self._energy -= 15
            move = int(self._speed * 1.5) + rand.randint(-1,1)
            movement = f"{self._name} uses Nitro Boost and moves {move} units!"
        else:
            move = 1
            movement = f"{self._name} is low on energy and only moves {move} unit."

        if obs_loc >= self._position:
            self._position = obs_loc
            movement = f"{self._name} crashed into an obstacle."
            return  movement
        else:
            self._position += self._speed + move
            return  movement

        
        
