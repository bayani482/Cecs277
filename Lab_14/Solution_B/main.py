"""
Lab 14 - state

Student 1: Brian Bayani
Student 2: Javier Jacobo
Date: December 1st, 2025

This program manages states of a puppy using the state design pattern.
"""

import check_input
from puppy import Puppy


def main():
    print("Congratulations on your new puppy!")
    puppy = Puppy()
    while True:
        print("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit")
        choice = check_input.get_int_range("Enter choice: ", 1, 3)
        
        if choice == 1:
            action = puppy.give_food()
        elif choice == 2:
            action = puppy.throw_ball()
        else:
            print("quitting...")
            break
        print(action)

if __name__ == "__main__":
    main()
