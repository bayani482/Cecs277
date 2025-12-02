"""
Lab 14 - State

Student 1: Brian Bayani
Student 2: Javier Jacobo
Date: Decemeber 1st, 2025

An awesome tomagachi style game implementing the state design pattern.

"""

from puppy import Puppy
import check_input

def main():
    puppy = Puppy()
    play = True

    print("Congratulations on your new puppy!")

    while play:
        user_choice = check_input.get_int_range("What would you like to do?\n1. Feed the puppy\n2. Play with the puppy\n3. Quit\nEnter choice: ",1,3)
        match user_choice:
            case 1:
                puppy.give_food()
            case 2:
                puppy.throw_ball()
            case 3:
                play = False
    
    print("Thanks for playing!")            



if __name__ == "__main__":
    main()