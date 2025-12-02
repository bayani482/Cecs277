"""

eat state for the puppy
"""
from puppy_state import PuppyState


class StateEat(PuppyState):
    def play(self, puppy):
        from state_play import StatePlay
        puppy.reset()
        puppy.change_state(StatePlay())
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."
    
    def feed(self, puppy):
        from state_asleep import StateAsleep
        puppy.inc_feeds()
        if puppy.feeds < 3:
            return  "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(StateAsleep())
            puppy.reset()
            return  "The puppy at so much it fell asleep."
        