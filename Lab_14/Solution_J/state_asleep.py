from puppy_state import PuppyState
from state_eat import StateEat

class StateAsleep(PuppyState):
    def play(self, puppy):
        return "The puppy is asleep and cannot play right now!"

    def feed(self, puppy):
        puppy.change_state(StateEat())
        return "The puppy is asleep but peaks it's eye open as you approach with food. It wakes up and devours the chow!"