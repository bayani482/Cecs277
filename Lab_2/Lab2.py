""" LAB 2
    09/03/2025

    Student 1: Javier Jacobo
    Student 2: Bryan Bayani

"""

import random as rand

import check_input


def get_users_bet(money):
    print(f"You have $ {money} dollars")
    bet = check_input.get_int_range("How much do you wanna bet? ", 1, money)
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
            print(f"you got lucky this time ...\n you have ${user_money} dollars")
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

