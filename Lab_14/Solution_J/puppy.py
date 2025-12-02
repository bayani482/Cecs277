from state_asleep import StateAsleep

class Puppy:
    def __init__(self):
        self._plays = 0
        self._feeds = 0
        self._state = StateAsleep()

    @property
    def plays(self):
        return self._plays
    
    @property
    def feeds(self):
        return self._feeds  
    
    def change_state(self, new_state):
        self._state = new_state
        self.reset()

    def throw_ball(self):
        self._state.play(self)
    
    def give_food(self):
        self._state.feed(self)

    def inc_feeds(self):
        self._feeds += 1

    def inc_plays(self):
        self._plays += 1

    def reset(self):
        self._feeds = 0
        self._plays = 0

    
