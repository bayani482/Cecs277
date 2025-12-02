"""

play state for the puppy.

"""
from puppy_state import PuppyState


class StatePlay(PuppyState):
    def play(self, puppy):
        from state_asleep import StateAsleep
        puppy.inc_plays()
        if puppy.plays < 3:
            return "You throw the ball again and the puppy excitedly chases it."
        else:
            puppy.change_state(StateAsleep())
            puppy.reset()
            return "The puppy is tired from playing and curls up for a nap."
    def feed(self, puppy):
        return  "The puppy is too busy with the ball to eat right now."
    