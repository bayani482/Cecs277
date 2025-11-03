from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll
import random as rand

class BegFactory(EnemyFactory):
    def create_random_enemy(self):
        enemy_type = rand.choice(['goblin','troll'])
        if enemy_type == 'goblin':
            return BegGoblin()
        else:
            return BegTroll()

