""" LAB 3
    09/08/2025

    Student 1: Javier Jacobo
    Student 2: Bryan Bayani

"""

import random as rand
from dictionary import words
import check_input_lab3

def display_gallows(num_incorrect):
    """
        Function that displays the proper gallows based on the number of incorrect guesses inputed by the user.
        INPUT: num_incorrect (Integer)
    """
    gallows = [
        """
                    ========
                    ||/    |
                    ||
                    ||
                    ||
                    """,
                    """
                    ========
                    ||/    |
                    ||     0
                    ||
                    ||
                    """,
                    """
                    ========
                    ||/    |
                    ||     0
                    ||     |
                    ||
                    """,
                    """
                    ========
                    ||/    |
                    ||     0
                    ||     |
                    ||    /
                    """,
                    """
                    ========
                    ||/    |
                    ||     0
                    ||     |
                    ||    / \\
                    """,
                    """
                    ========
                    ||/    |
                    ||    \\0
                    ||     |
                    ||    / \\
                    """,
                    """
                    ========
                    ||/    |
                    ||    \\0/
                    ||     |
                    ||    / \\
                    """
        ]
    print(gallows[num_incorrect])

def display_letters(letters):
    """
        Function to display the remaining alphabetical letters the user may choose from
        INPUT: letters (List)
    """
    print("Letters remaining: ")
    for i in letters:
        print(i, end=" ")

def get_letters_remaining(incorrect, correct):
    """
        Function that iterates through both "incorrect" and "correct" lists, finding and removing their elements from the "alpha" (Alphabet) list.
        INPUT: incorrect, correct (Lists)
        OUTPUT: alpha (list)
    """
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in incorrect:
        if letter in alpha:
            alpha.remove(letter)
    for letter in correct:
        if letter in alpha:
            alpha.remove(letter)
    return alpha


def main():

    play = True

    while play:
        rand_word = rand.choice(words)
        incorrect = []
        correct = ["_","_","_","_","_"]
        incorrect_count = 0
        correct_count = 0

        # To debug, uncomment the following line of code below:
        # print(rand_word)

        while incorrect_count < 6:
            print(f"Incorrect selections: {' '.join(incorrect)}")
            display_gallows(incorrect_count)
            display_letters(get_letters_remaining(incorrect, correct))
            print()
            print(" ".join(correct))
            print()

            guess = check_input_lab3.get_alpha("Enter a letter: ")

            # Verify if guess has already been guessed
            if guess in incorrect or guess in correct:
                print("You already guessed that letter!\n")
                continue

            if guess in rand_word:
                print("Correct!\n")
                # Reveal all positions of the guessed letter
                for i, letter in enumerate(rand_word):
                    if letter == guess:
                        correct[i] = guess
                correct_count += 1
            else:
                print("Incorrect!\n")
                incorrect.append(guess)
                incorrect_count += 1
            
            # If user guesses entire word correctly display results
            if "_" not in correct:
                display_gallows(incorrect_count)
                print(" ".join(correct))
                print()
                print(f"You win! The word was {rand_word}.")
                break
        
        # If user reaches maximum amount of guesses allowed, the user loses and results are displayed
        if incorrect_count == 6:
            display_gallows(incorrect_count)
            print(" ".join(correct))
            print()
            print(f"You lose! The word was {rand_word}.")

        play = check_input_lab3.get_yes_no("Do you wonna play again? (Y/N): ")

if __name__ == '__main__':
    main()
