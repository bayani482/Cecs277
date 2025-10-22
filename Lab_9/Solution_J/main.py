from basic_door import BasicDoor
from door import Door
import check_input


def open_door(door):
    print(door._state)  # For testing purposes, to know the correct option
    print(door.examine_door())
    while not door.is_unlocked():
        print(door.menu_options())
        option = check_input.get_int_range(">",1,door.get_menu_max())
        door.attempt(option)
    print(door.success())

def main():
    basic_door = BasicDoor()
    open_door(basic_door)

if __name__ == "__main__":
    main()