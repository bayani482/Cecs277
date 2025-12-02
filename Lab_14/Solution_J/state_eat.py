from puppy_state import PuppyState
from state_play import StatePlay

class StateEat(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feeds >= 3:
            puppy.change_state(StateAsleep())
            return "The puppy is full and tired now. It falls back to sleep."
        else:
            return "The puppy eagerly eats the food!"

    def play(self, puppy):
        puppy.change_state(StatePlay())
        return "Despite just eating, the puppy wants to play now!"

