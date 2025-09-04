""" LAB 2
    09/03/2025

    Student 1: Javier Jacobo
    Student 2: Bryan Bayani



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
    print(f"You have ${money}.")
    bet = check_input.get_int_range("How much do you wanna bet? ", 1, money)
    return bet

def get_users_choice():
    """
    def get_users_choice():
    “““ prints to screen 3 cards for the game, takes in user input and validates it between 1-3

    Returns:
        returns the validated user choice
    """
    
    print("""
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
        x (int): int value between 1-3 of location of the queen
    """
    if queen_loc ==1:
        position_1 = "Q"
        position_2 = "K"
        position_3  = "K"
    elif queen_loc == 2:
        position_1  = "K"
        position_2 = "Q"
        position_3  = "K"
        
    elif queen_loc == 3:
        position_1  = "K"
        position_2  = "K"
        position_3  = "Q"
        
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print(f"|  {position_1}  | |  {position_2}  | |  {position_3}  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")
    

def main():
    print("-- Three Card Monte --")
    print("Find the queen to double your bet!")
    play = True
    user_money = 100

    while play:
        queenLoc = rand.randint(1,3)
        print(queenLoc)
        bet = get_users_bet(user_money)
        users_Choice = get_users_choice()
        display_queen_loc(queenLoc)
        if queenLoc == users_Choice:
            user_money += bet
            print(f"you got lucky this time ...\n you have ${user_money}.")
        else:
            user_money -= bet
            print("Sorry... you lose")
        
        if user_money == 0:
            print("You're out of money. Beat it loser!")
            play = False
        else:
            play = check_input.get_yes_no("Wanna play again? Y/N: ")

if __name__ == '__main__':
    main()

