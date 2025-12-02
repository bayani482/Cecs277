"""
Abstract Factory for Creating Enemy Instances

"""
import abc


class EnemyFactory(abc.ABC):
    @abc.abstractmethod
    def create_random_enemy(self):
        """
        Creates a random enemy instance.
        Returns:
            object: an instance of an enemy
        """
        pass

