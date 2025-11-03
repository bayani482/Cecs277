"""
Lab 11 - Factory

Student 1: Bryan Bayani
Student 2: Javier Jacobo
Date: November 5th, 2025


"""

from hero import Hero
from enemy_factory import EnemyFactory
from beg_factory import BegFactory
from exp_factory import ExpFactory
import check_input


def main():
    print("Monster Trials")
    name = input("What is your name? >")
    print(f"You will face a series of 3 monsters, {name}.\nDefeat them all to win.")

    exp_fact = ExpFactory()
    beg_fact = BegFactory()
    hero = Hero(name)
    enemy1 = beg_fact.create_random_enemy()
    enemy2 = beg_fact.create_random_enemy()
    enemy3 = exp_fact.create_random_enemy()

    enemies = [enemy1, enemy2, enemy3]

    defeated = 0

    while defeated < 3:
        print("Choose an enemy to attack:")
        for i, enemy in enumerate(enemies):
            print(f"{i + 1}. {str(enemy)}")

        enemy_choice = check_input.get_int_range("Enter choice: ", 1, len(enemies))
        chosen_enemy = enemies[enemy_choice - 1]

        
        
        

if __name__ == "__main__":
    main()