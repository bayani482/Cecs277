
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

        move = max(1, move)
        
        if obs_loc is None:
            self._position += move
            if self._position > 100:
                self._position = 100
            return movement

        if move >= obs_loc:
            move = obs_loc
            self._position += move
            if self._position > 100:
                self._position = 100
            return f"{self._name} crashed into an obstacle."
        
        self._position += move
        return  movement

