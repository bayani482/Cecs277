""" LAB 1
    08/25/2025

    Student 1: Javier, Jacobo
    Student 2: Brian, Bayani
    
    Creates a random integer between (1-100).
    Checks input validity via check_input module.
    Keeps count of all valid guesses user makes.

    Args:
        Guess (int): User inputted integer
        Random_integer (int): Random generated integer within range 1-100
    Returns:
        Number of valid tries user made
    Changes to check_input.py:
        Added lines of code 81 & 84 to prompt the user "Guess again (1-100) when inputting invalid data.
"""

import random as rand
import check_input

if __name__ == '__main__':
    random_int = rand.randint(1,100)

    # To debug/see random integer use this following line of code:
    # print(random_int)

    guess = check_input.get_int_range("Im thinking of a number. Make a guess (1-100): ", 1, 100)
    
    tries = 1

    while guess != random_int:

        if guess < random_int:
            guess = check_input.get_int_range("Too low! Guess again (1-100): ", 1, 100)
            tries += 1

        else:
            guess = check_input.get_int_range("Too high! Guess again (1-100): ", 1, 100)
            tries += 1

    print(f"Congrats! it only took you {tries} tries!")
