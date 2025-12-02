"""
Puppy class

"""
from state_asleep import StateAsleep


class Puppy:
    def __init__(self):
        """
        Initialize a Puppy instance
        """
        self._state = StateAsleep()
        self._plays = 0
        self._feeds = 0

    @property
    def plays(self):
        """
        Get the number of plays
        
        Returns:
            int: The number of plays
        """
        return self._plays
    @property
    def feeds(self):
        """
        Get the number of feeds
        Returns:
            int: The number of feeds
        """
        return self._feeds

    def change_state(self, new_state):
        """
        Change the state of the puppy
        
        Args:
            new_state (str): The new state to set for the puppy
        """
        self._state = new_state

    def throw_ball(self):
        """
        calls the play method for what state the puppy currently is in
        
        """
        return self._state.play(self)

    def give_food(self):
        """
        Simulate giving food to the puppy
        
        Returns:
            str: A message indicating the puppy's reaction
        """
        return self._state.feed(self)

    def inc_feeds(self):
        """
        icrements the puppy's feed count in a row
        
        Returns:
            str: A message indicating the puppy's reaction
        """
        self._feeds += 1

    def inc_plays(self):
        """
        Simulate increasing the puppy's playtime
        
        Returns:
            str: A message indicating the puppy's reaction
        """
        self._plays += 1

    def reset(self):
        """
        Reset the puppy's state to a default
        
        """
        self._plays = 0
        self._feeds = 0
        