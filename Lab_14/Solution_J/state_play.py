from puppy_state import PuppyState
from state_asleep import StateAsleep

class StatePlay(PuppyState):
    def play(self, puppy):
        puppy.inc_plays()
        if puppy.plays >= 3:
            puppy.change_state(StateAsleep())
            return "The puppy is exhausted from playing and falls back to sleep."
        return "The puppy happily plays with you!"    

    def feed(self, puppy):
        return "The puppy is already playing and is too dumb to eat right now!"

    
    