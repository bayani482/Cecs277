"""

eat state for the puppy

"""
from puppy_state import PuppyState


class StateEat(PuppyState):
    """
    eat state of puppy

    Args:
        PuppyState (object): puppy object
    """
    def play(self, puppy):
        """play method

        Args:
            puppy (_type_): _description_

        Returns:
            str: string message of puppies state
        """
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
                