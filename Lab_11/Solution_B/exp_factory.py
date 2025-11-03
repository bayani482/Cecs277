"""_summary_
"""
import random as rand

from enemy_factory import EnemyFactory


class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        randomEnemy=rand.randint(0,2)
        match randomEnemy:
            case 1:
                return "ExpGoblin"
            case 2:
                return "ExpTroll"

    