"""
LAB 7

Student 1: Javier Jacobo
Student 2: Bryan Bayani

Basic rpg program to display inheritence in classes

"""
import random as rand

import check_input
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
from hero import Hero


def main():
    name = input("What is your name, challenger?\n> ")
    hero = Hero(name,50)
    dragons = [Dragon("Deadly Nadder",10),FireDragon("Gronckle",15),FlyingDragon("Timberjack",20)]
    print(f"Welcome to dragon training, {hero._name}\nYou must defeat 3 dragons.")
    play = True

    while play:
        print(f"\n{hero}")
        if hero._hp <= 0:
            print("You have been defeated")
            play = False
            break
        
        for key,value in enumerate(dragons):
            print(f"{key+1}. Attack {str(value)}")
        
        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ",1,len(dragons))
        target = dragons[dragon_choice - 1]
        # Uncomment below to see what dragon you are attacking.
        # print(f"You have chosen to attack {target._name}")
        attack_choice = check_input.get_int_range("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)\nEnter weapon: ",1,2)
                
        match attack_choice:
            case 1:
                print(hero.arrow_attack(target))
            case 2:
                print(hero.sword_attack(target))

        dragon_attack = rand.randint(1,2)

        random_dragon = rand.choice(dragons)

        match dragon_attack:
            case 1:
                print(random_dragon.basic_attack(hero))
            case 2:
                print(random_dragon.special_attack(hero))
            
        if target._hp <= 0:
            print(f"You have defeated the {target._name}!")
            dragons.remove(target)
            if len(dragons) == 0:
                print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")
                play = False
                break
                
if __name__ == '__main__':
    main()

