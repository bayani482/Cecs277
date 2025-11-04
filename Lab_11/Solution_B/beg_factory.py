"""_summary_
"""
import random as rand

from beg_goblin import BegGoblin
from beg_troll import BegTroll
from enemy_factory import EnemyFactory


class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        randomEnemy=rand.randint(0,2)
        match randomEnemy:
            case 1:
                return BegGoblin()
            case 2:
                return BegTroll()

    