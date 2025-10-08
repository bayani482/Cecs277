"""
LAB 7

Student 1: Javier Jacobo
Student 2: Bryan Bayani

Basic rpg program to display inheritence in classes

"""
import random as rand
from hero import Hero
from dragon import Dragon
from flying import FlyingDragon
from fire import FireDragon
import check_input

def main():
    name = input("What is your name, challenger?\n> ")
    hero = Hero(name,50)
    dragons = [Dragon("Deadly Nadder",10),FireDragon("Gronckle",15),FlyingDragon("Timberjack",20)
               ]
    print(f"Welcome to dragon training, {hero._name}\nYou must defeat 3 dragons.")
    play = True

    while play:
        print(f"\n{hero}")
        if hero._hp <= 0:
            print("You have been defeated")
            play = False
            break

            
        if len(dragons) == 0:
            print("All dragons are dead")
            play = False

        for key,value in enumerate(dragons):
            print(f"{key+1}. Attack {str(value)}")
        
        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ",1,len(dragons))
        attack_choice = check_input.get_int_range("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)\nEnter weapon: ",1,2)
        target = dragons[dragon_choice - 1]

        match attack_choice:
            case 1:
                print(hero.arrow_attack(target))
            case 2:
                print(hero.sword_attack(target))
            
        if target._hp <= 0:
            print(f"You have defeated the {target._name}!")
            dragons.remove(target)
            if len(dragons) == 0:
                print("All dragons are dead")
                play = False
                break
                
            
        random_dragon = rand.randint(0,len(dragons)-1)
        print(dragons[random_dragon].special_attack(hero))

if __name__ == '__main__':
    main()
