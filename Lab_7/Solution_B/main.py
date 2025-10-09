"""
LAB 7
Main.py

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This is a program that allows a user to input there name and fight 3 different types of dragons.
"""

import random as rand

import check_input
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
from hero import Hero


def main():
    dragons = [
        Dragon("Deadly Nadders", 10),
        FireDragon("Gronckle", 15),
        FlyingDragon("Timberjack", 20)
    ]
    name = input("What is your name, challenger?\n").capitalize()
    print(f"Welcome to dragon training, {name}\nYou must defeat 3 dragons.\n")
    hero = Hero(name, 50)
    play = True
    while play:
        print(hero)
        for i, dragon in enumerate(dragons):
            print(f"{i+1}. {dragon}")

        select_dragon = int(check_input.get_int_range(f"Choose a dragon to attack:", 1, len(dragons)))
        match select_dragon:
            case 1:
                dragon = dragons[0]
                
            case 2:
                dragon = dragons[1]
                
            case 3:
                dragon = dragons[2]

        hero_attack = int(check_input.get_int_range(f"Attack with:\n1. Arrow (1 D12)\n2. Sword(2 D6)\nEnter Weapon: ",1,2))
        match hero_attack:
            case 1:
                print(hero.arrow_attack(dragon))
            case 2:
                print(hero.sword_attack(dragon))

        if dragon.hp <= 0:
            print(f"You have defeated the {dragon.name}!")
            dragons.remove(dragon)
            if len(dragons) == 0:
                break
            else:
                dragon = rand.choice(dragons)
            
        dragon_attack = rand.randint(1,2)
        match dragon_attack:
            case 1:
                print(dragon.basic_attack(hero))
            case 2:
                print(dragon.special_attack(hero))
        if hero.hp <= 0:
            play = False
            
        
    if hero.hp <= 0:
        print("\nYou have been defeated, you need more training")
    else:
        print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")
    
if __name__ == '__main__':
    main()