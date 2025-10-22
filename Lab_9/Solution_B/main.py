"""
LAB 9

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This program is a game that allows the user to unlock different doors by selecting from the menu.

"""

import random as rand

import check_input
from basic_door import BasicDoor
from combo_door import ComboDoor
from deadbolt_door import Deadbolt


def open_door(door):
    print(door.examine_door())
    while not door.is_unlocked():
        print(door.menu_options())
        option = check_input.get_int_range(f"Enter your Choice: 1-{int(door.get_menu_max())}:",1, door.get_menu_max())
        door.attempts(option)
        if door.is_unlocked():
            print(door.success())
        else:
            print(door.clue())

def main():
    print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...")
    door_types = [BasicDoor,Deadbolt, ComboDoor]

    for i in range(len(door_types)):
        door = rand.choice(door_types)()
        open_door(door)
    print("Congratulations! You escaped...this time.")
if __name__ == "__main__":
    main()