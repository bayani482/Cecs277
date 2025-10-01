"""
LAB 6

Student 1: Javier Jacobo
Student 2: Bryan Bayani

Basic Roll Program using Composititon Relation

"""

from die import Die
from player import Player
import check_input

def take_turn(player):
    Player.roll_dice(player)
    print(str(player))

    if Player.has_three_of_a_kinda(player):
        print("You have 3 of a kind!")
        print(f"Score = {player._points}")
    elif Player.has_pair(player):
        print("You have a pair!")
        print(f"Score = {player._points }")
    elif Player.has_series(player):
        print("You have a series of 3!")
        print(f"Score = {player._points}")
    else:
        print("Aww too bad. No points earned :(")
        print(f"Score = {player._points}")

def main():
    player = Player()
    print("--Yahtzee--")
    play = True

    while play:
        take_turn(player)
        play = check_input.get_yes_no("Play again? (Y/N): ")

    print("\nGame Over")
    print(f"Final Score = {player._points}")

if __name__ == '__main__':
    main()
