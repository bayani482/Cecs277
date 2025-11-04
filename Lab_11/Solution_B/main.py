"""_summary_
"""

import beg_factory as BegFactory
import check_input
import exp_factory as ExpFactory
import hero

def main():
    hero_name = input("Monster Trials\nWhat is your name? ")
    print(f"You will face a series of 3 monsters, {hero_name}.\nDefeat them all to win.")
    hero = hero(hero_name, 30)
    
if __name__ == "__main__":
    main()