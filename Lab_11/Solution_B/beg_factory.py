"""
beg_factory.py: Beginner Factory Class

"""
import random as rand

from beg_goblin import BegGoblin
from beg_troll import BegTroll
from enemy_factory import EnemyFactory


class BegFactory(EnemyFactory):
    def create_random_enemy(self):
        """
        Creates a random beginner enemy.
        Returns:
            object: an instance of a beginner enemy
        """
        randomEnemy=rand.choice([1,2])
        match randomEnemy:
            case 1:
                return BegGoblin()
            case 2:
                return BegTroll()
