"""
Student 1: Bryan Bayani
Student 2: Javier Jacobo

Lab 10 - Singletons
Date: October 28th, 2025

"""

from hero import Hero
from enemy import Enemy
from map import Map
import check_input
import random as rand

def main():
    game_map = Map()
    hero_name = input("Enter the name of your hero: ")
    hero = Hero(hero_name)
    print(f"Welcome, {hero_name}! Your adventure begins now.")

    while True:
        print(hero)
        game_map.show_map(hero.loc)
        
        print("Choose a direction to move:")
        print("1. North")
        print("2. South")
        print("3. East")
        print("4. West")

        choice = check_input.get_int_range("Enter your choice (1-4): ", 1, 4)
        
        match choice:
            case 1:
                current_tile = hero.go_north()
            case 2:
                current_tile = hero.go_south()
            case 3:
                current_tile = hero.go_east()
            case 4:
                current_tile = hero.go_west()

        if current_tile == 'm':  # Monster
            enemy = Enemy()
            print(f"A wild {enemy.name} appears!")
            print(enemy)
            
            while enemy.hp > 0:
                print("\nWhat would you like to do?")
                print("1. Attack")
                print("2. Run away")
                action = check_input.get_int_range("Enter your choice (1-2): ", 1, 2)
                
                match action:
                    case 1:  # Attack
                        hero.attack(enemy)
                        if enemy.hp > 0:
                            enemy.attack(hero)
                            if hero.hp <= 0:
                                print("You have been defeated! Game Over.")
                                return
                        else:
                            print(f"You defeated the {enemy.name}!")
                            game_map.remove_at_loc(hero.loc)  # Remove 'm' from map
                            break
                    case 2:  # Run away
                        print("You run away in a random direction!")
                        directions = ['north', 'south', 'east', 'west']
                        random_dir = rand.choice(directions)
                        
                        if random_dir == 'north':
                            hero.go_north()
                        elif random_dir == 'south':
                            hero.go_south()
                        elif random_dir == 'east':
                            hero.go_east()
                        elif random_dir == 'west':
                            hero.go_west()
                        
                        print(f"You ran {random_dir}!")
                        break  # Exit the monster encounter
                    
        elif current_tile == 'n':  # Nothing/empty room
            print("This room is empty. You can move freely.")
        
        elif current_tile == 'o':  # Wall
            print("You hit a wall! You cannot move in that direction.")
            
        elif current_tile == 's':  # Start
            print("You wound up back at the start of the dungeon.")
            
        elif current_tile == 'i':  # Item room - health potion
            hero.heal(25)
            print(f"You found a health potion and restored your health.")
            game_map.remove_at_loc(hero.loc)  # Remove 'i' from map

        elif current_tile == 'f':  # Finish
            print("Congratulations! You found the way out of the maze and won the game!")
            break

if __name__ == "__main__":
    main()  