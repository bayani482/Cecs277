"""
Expert Factory Class
"""
import random as rand

from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll


class ExpFactory(EnemyFactory):
    def create_random_enemy(self):
        """
        Creates a random expert enemy.
        Returns:
            object: an instance of an expert enemy
        """
        randomEnemy=rand.choice([1,2])
        match randomEnemy:
            case 1:
                return ExpGoblin()
            case 2:
                return ExpTroll()

    