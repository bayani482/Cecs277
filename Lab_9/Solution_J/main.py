""" LAB 9
    10/22/2025

    Student 1: Javier, Jacobo
    Student 2: Brian, Bayani
    
    Creates an escape room game with 3 types of doors:
    Basic Door, Locked Door, and Combo Door.
    Each door type has its own mechanics for unlocking.
    The player must unlock 3 doors to escape the room.
    
"""

from basic_door import BasicDoor
from combo import ComboDoor
from locked_door import LockedDoor
import check_input
import random as rand   


def open_door(door):
    """Function to handle the process of opening a door.
    Args:
        door (Door): An instance of a Door subclass.
    """
    print(door.examine_door())
    while not door.is_unlocked():
        print(door.menu_options())
        option = check_input.get_int_range(">", 1, door.get_menu_max())
        print(door.attempt(option))
        if door.is_unlocked():
            print(f"{door.success()}\n")
        else:
            print(f"{door.clue()}\n")

def main():
    doors_unlocked = 0

    print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...")
    while doors_unlocked < 3:
        doors = [LockedDoor(),ComboDoor(),BasicDoor()]
        open_door(rand.choice(doors))
        doors_unlocked += 1

    print("Congratulations! You have escaped... this time.")
if __name__ == "__main__":
    main()