"""
puppy state interface

"""
import abc


class PuppyState(abc.ABC):
    """
    Puppy state interface abstract class
    """
    @abc.abstractmethod
    def play(self,puppy):
        """
        Simulate throwing a ball to the puppy
        
        Returns:
            str: A message indicating the puppy's reaction
        """
        pass
    @abc.abstractmethod
    def feed(self,puppy):
        """
        Simulate giving food to the puppy
        
        Returns:
            str: A message indicating the puppy's reaction
        """
        pass

