from basic_door import BasicDoor
from combo import ComboDoor
from deadbolt import DeadboltDoor
from door import Door
import check_input
import random as rand   


def open_door(door):
    print(door.examine_door())
    while not door.is_unlocked():
        print(door.menu_options())
        option = check_input.get_int_range(">", 1, door.get_menu_max())
        print(door.attempt(option))
        
        if not door.is_unlocked():
            print(door.clue())

    print(f"{door.success()}\n")

def main():
    doors_unlocked = 0

    print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...")
    while doors_unlocked < 3:
        doors = [BasicDoor(), ComboDoor(), DeadboltDoor()]
        open_door(rand.choice(doors))
        doors_unlocked += 1

    print("Congratulations! You have escaped... this time.")
if __name__ == "__main__":
    main()