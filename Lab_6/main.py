"""
LAB 5

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This program is a game that rolls three dice and checks for either a pair, series, or three of a kind. You will earn points based on
what combination you roll. The user can play as many times as they want awnser Y to continue or N to stop.

"""
import check_input
from player import Player


def take_turn(player):
    """this function takes a player object and rolls the dice then checks for combinations and prints the results

    Args:
        player (list): list of three rolls
    """
    print("\n-Yahtzee-")
    player.roll_dice()
    print(player)
    if player.has_three_of_a_kind():
        print(f"Three of a Kind of {player._dice[0]._value}!")
    elif player.has_series():
        print(f"You got a Series of {player._dice[0]._value}!")
    elif player.has_pair():
        print("You got a Pair!")
    else:
        print("Aww. Too Bad.")
        
    print(f"Score: {player._points}")
    
def main():
    player = Player()
    play = True
    while play == True:
        take_turn(player)
        play = check_input.get_yes_no("Play again? (Y/N): ")


    print(f"\nGame Over.\nFinal Score = {player._points}\n")

if __name__ == "__main__":
    main()