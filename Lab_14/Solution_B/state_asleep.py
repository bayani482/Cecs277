"""
asleep state for the puppy

"""
from puppy_state import PuppyState


class StateAsleep(PuppyState):
    """
    puppy asleep state

    Args:
        PuppyState (object): puppy object
    """
    def play(self, puppy):
        return "The puppy is asleep and doesn't want to play right now."
    def feed(self, puppy):
        from state_eat import StateEat
        puppy.reset()
        puppy.change_state(StateEat())
        puppy.inc_feeds()
        return  "The puppy wakes up and comes running to eat."
    


