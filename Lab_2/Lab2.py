""" LAB 2
    09/03/2025

    Student 1: Javier Jacobo
    Student 2: Bryan Bayani

"""

import random as rand
import check_input

def get_users_bet(money):
    print(f"You have $ {money} dollars")
    bet = check_input.get_int_range("How much do you wonna bet? ", 1, money)
    get_users_choice()
    return bet

def get_users_choice():
    print("""
+-----+ +-----+ +-----+
|     | |     | |     |
|  1  | |  2  | |  3  |
|     | |     | |     |
+-----+ +-----+ +-----+""")
    user_choice = check_input.get_int_range("Find the queen: ", 1, 3)
    return user_choice
    


def display_queen_loc(queen_loc):

def main():
    print("-- Three Card Monte --")
    print("Find the queen to double your bet!")
    play = True
    user_money = 100


    while play:
        get_users_bet(user_money)
        play = check_input.get_yes_no("Wonna play again? Y/N: ")

if __name__ == '__main__':
    main()
