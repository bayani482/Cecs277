import random as rand

from vehicle import Vehicle


class Motorcycle(Vehicle):
    def slow(self, obs_loc):
            move = int(self._speed * 0.75) + rand.randint(-1, 1)
            if self._position + move >= obs_loc:
                distance = obs_loc - self._position
                self._position = self._position + move
                movement = f"{self._name} slowly dodges the obstacle and moves {distance} units."
                return movement
            else:
                self._position += move
                movement = f"{self._name} moves slowly {move} units."
                return movement

    def special_move(self, obs_loc):
        if self._energy >= 15:
            self._energy -= 15
            if rand.random() <= 0.75:
                move = int(self._speed * 2) + rand.randint(-1, 1)
                if self._position + move >= obs_loc:
                    distance = obs_loc - self._position
                    self._position = obs_loc
                    movement = f"{self._name} tries a wheelie and crashes into an obstacle moving {distance} units!"
                    return movement
                else:
                    self._position += move
                    movement = f"{self._name} does a wheelie and moves {move} units!"
                    return movement
            else:
                self._position += 1
                movement = f"{self._name} tries a wheelie but falls over and only moves 1 unit."
                return movement
        else:
            self._position += 1
            movement = f"{self._name} doesn't have enough energy for a wheelie and only moves 1 unit."
            return movement