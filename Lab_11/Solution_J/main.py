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
    name = input("What is your name? > ")
    print(f"You will face a series of 3 monsters, {name}.\nDefeat them all to win.")

    exp_fact = ExpFactory()
    beg_fact = BegFactory()
    hero = Hero(name)
    enemy1 = beg_fact.create_random_enemy()
    enemy2 = beg_fact.create_random_enemy()
    enemy3 = exp_fact.create_random_enemy()

    enemies = [enemy1, enemy2, enemy3]

    defeated = 0

    while defeated < 3 and hero._hp > 0:
        print("\nChoose an enemy to attack:")
        for i, enemy in enumerate(enemies):
            print(f"{i + 1}. {str(enemy)}")

        enemy_choice = check_input.get_int_range("Enter choice: ", 1, len(enemies))
        chosen_enemy = enemies[enemy_choice - 1]

        attack_choice = check_input.get_int_range(f"\n{str(hero)}\n1. Melee Attack\n2. Ranged Attack\nEnter choice: ", 1, 2)

        print()
        match attack_choice:
            case 1:
                print(hero.melee_attack(chosen_enemy))
            case 2:
                print(hero.ranged_attack(chosen_enemy))
        
        if enemy._hp > 0:
            print(enemy.melee_attack(hero))
        elif enemy._hp <= 0:
            print(f"{enemy._name} has been slain!\n")
            enemies.pop(enemy_choice - 1)
            print(hero)

    if hero._hp <= 0:
        print("You have been slain. Game over.")
    else:
        print("Congratulations! You defeated all three monsters!\nGame Over")

if __name__ == "__main__":
    main()