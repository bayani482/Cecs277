from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
import random as rand

class ExpFactory(EnemyFactory):
    def create_random_enemy(self):
        enemy_type = rand.choice(['goblin','troll'])
        if enemy_type == 'goblin':
            return ExpGoblin()
        else:
            return ExpTroll()
        
