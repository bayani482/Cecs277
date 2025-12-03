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
        abstract play method
        
        Returns:
            str: A message indicating the puppy's playing
        """
        pass
    @abc.abstractmethod
    def feed(self,puppy):
        """
        abstract feed method
        
        Returns:
            str: A message indicating the puppy's eating
        """
        pass

