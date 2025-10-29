"""
LAB 10

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This program is a game that allows the user to explore a map and fight monsters.

"""
import random as rand

import check_input
from enemy import Enemy
from hero import Hero
from map import Map


def main():
    name = input("What is your name, traveler? ").strip().capitalize()
    hero = Hero(name)
    game_map = Map()
    game_map.reveal(hero.loc)

    
    playing = True
    while playing:
        print(f"\n{hero.name}: {hero.hp}/{hero.max_hp} HP")
        print(game_map.show_map(hero.loc))
        print("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
        choice = check_input.get_int_range(f"Enter your choice (1-5): ",1, 5)
        match choice:
            case 1:
                tile = hero.go_north()
            case 2:
                tile = hero.go_south()
            case 3:
                tile = hero.go_east()
            case 4:
                tile = hero.go_west()
            case 5:
                break

        game_map.reveal(hero.loc)
        if tile == "m":
            print("You encounter a MONSTER!")
            enemy = Enemy()
            print(enemy)
            while enemy.hp > 0:
                action = check_input.get_int_range("\n1. Attack\n2. Run Away\nChoose your action (1-2): ", 1, 2)
                match action:
                    case 1: # Hero attacks
                        print(hero.attack(enemy))
                        if enemy.hp <= 0:
                            print(f"You have slain a {enemy.name} ")
                            game_map.remove_at_loc(hero.loc)
                            break
                        print(enemy.attack(hero))# Enemy attacks back
                        if hero.hp <= 0:
                            print("You have been slain Game Over.")
                            playing = False
                            break
                    case 2:# Run away in random direction
                        direction = rand.choice(["north", "south", "east", "west"])
                        print(f"You run away and ran {direction}.")
                        match direction:
                            case "north":
                                hero.go_north()
                            case "south":
                                hero.go_south()
                            case "east":
                                hero.go_east()
                            case "west":
                                hero.go_west()
                        game_map.reveal(hero.loc)
                        print(game_map.show_map(hero.loc))
                        break
        elif tile == "n":
            print("There is nothing here...")
        elif tile == "s":
            print("You wound up back at the start of the dungeon.")
        elif tile == "i":
            print("You found a health potion!")
            if hero.hp == hero.max_hp:
                print("You're already at full health. You save it for later.")
            else:
                hero.heal()
                print("You drink it to restore your health")
                game_map.remove_at_loc(hero.loc)
        elif tile == "f":
            print("Congratulations! You found the exit and escaped the dungeon!")
            playing = False
        elif tile == "o":
            print("You can’t move in that direction.")
    print("\nGame Over")

if __name__ == "__main__":
    main()
