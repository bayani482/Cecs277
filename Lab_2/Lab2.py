""" LAB 2
    09/03/2025

    Student 1: Javier Jacobo
    Student 2: Bryan Bayani

This is a gambling game where the user needs to wager money and select a one of three cards where the queen is located. 
Each of the user input is validated. The user can decide to continue playing after each play or until they run out of money.


"""

import random as rand

import check_input

def get_users_bet(money):
    """
    takes in a integer of users money as an argument, displays users money, takes in user input of betting amount and validaties it.

    Args:
        x (int): int value of user input

    Returns:
        returns user bet in
    """

    print(f"\nYou have ${money}")
    bet = check_input.get_int_range("How much do you wonna bet? ", 1, money)
    return bet

def get_users_choice():
    """
    def get_users_choice():
    “““ prints to screen 3 cards for the game, takes in user input and validates it between 1-3

    Returns:
        returns the validated user choice
    """

    print(
"""
+-----+ +-----+ +-----+
|     | |     | |     |
|  1  | |  2  | |  3  |
|     | |     | |     |
+-----+ +-----+ +-----+""")
    user_choice = check_input.get_int_range("Find the queen: ", 1, 3)
    return user_choice
    
def display_queen_loc(queen_loc):

    """
    Prints out to screen location of the queen

    Args:
        queen_loc (list): List with location of queen at randomly generated index (0-2) from main.
    """
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print(f"|  {queen_loc[0]}  | |  {queen_loc[1]}  | |  {queen_loc[2]}  |")    # Print out all elements of the "queen_list" list.
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

def main():
    print("-- Three Card Monte --")
    print("Find the queen to double your bet!")
    print("-----------------------------------")
    play = True
    user_money = 100

    while play:

        queen_list = ["K","K","K"]  # Create/Reset a list named "queen_list" of 3 elements, all "K".
        queen_location = rand.randint(1,3)
        queen_list[queen_location - 1] = "Q"    #Change index at "queen_location" (random number from 1-3)

        # To debug and find the queen's location, uncomment the line of code below
        print(f"Queen's Location: {queen_location}")

        bet = get_users_bet(user_money)
        users_Choice = get_users_choice()
        display_queen_loc(queen_list)

        if queen_location == users_Choice:
            user_money += bet
            print(f"You got lucky this time ...\n")
        else:
            user_money -= bet
            print("Sorry... you lose\n")
        
        if user_money == 0:
            print("You're out of money. Beat it loser!")
            play = False
        else:
            play = check_input.get_yes_no("Wanna play again? Y/N: ")

if __name__ == '__main__':
    main()