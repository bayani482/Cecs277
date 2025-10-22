from basic_door import BasicDoor
from combo import ComboDoor
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
    
    print(door.success())

def main():
    doors_unlocked = 0

    while doors_unlocked < 3:
        doors = [BasicDoor(), ComboDoor()]
        open_door(rand.choice(doors))
        doors_unlocked += 1

if __name__ == "__main__":
    main()