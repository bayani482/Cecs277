"""LAB 3
09/08/2025

Student 1: Javier Jacobo
Student 2: Bryan Bayani

"""

import random as rand

import check_input_lab3
from dictionary import words


def display_gallows(num_incorrect):
    """
    display_gallows takes in a int and prints out the index of the game state
    Input: num_incorrect - int
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
        """,
    ]

    print(gallows[num_incorrect])

def display_letters(letters):
    """
    display_letters takes list and and prints out all the elements in a single string 
    Input: letters - list
    """
    print(" ".join(letters))

def get_letters_remaining(correct, incorrect):
    """
    get_letters_remaining takes in two lists which the user has guessed and removes the matches from alpha list. then return the alpha list
    Input: correct - list
            incorrect - list
    """
    alpha = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    for char in correct:
        if char != "_" and char in alpha:
            alpha.remove(char)

    for char in incorrect:
        if char in alpha:
            alpha.remove(char)

    return alpha


def main():
    alpha = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    play = True
    print("_________")

    while play:
        rand_word = rand.choice(words)
        incorrect = []
        correct = ["_", "_", "_", "_", "_"]
        incorrect_count = 0
        correct_count = 0
        display_gallows(incorrect_count)
        display_letters(correct)
        print("Remaining letters:", " ".join(get_letters_remaining(correct, incorrect)))

        #print(rand_word)
        while incorrect_count < 6:
            while True:
                guess = check_input_lab3.get_alpha("Guess a letter: ")
            
                if guess in correct or guess in incorrect:
                    print("You already guessed that letter. Try another.")
                else:
                    break
            
            if guess in rand_word:
                for i in range(len(rand_word)):
                    if rand_word[i] == guess and correct[i] == "_":
                        correct[i] = guess
                        correct_count += 1
                print("correct!")
            else:
                incorrect.append(guess)
                incorrect_count += 1
                print("Incorrect!")

            display_gallows(incorrect_count)
            display_letters(correct)
            print(
                "Remaining letters:",
                " ".join(get_letters_remaining(correct, incorrect)),
            )
            print(f"Incorrect selections: {' '.join(incorrect)}")
            if correct_count == len(rand_word):
                print("You Win!")
                break
            if incorrect_count == 6:
                print(f"You Lose! The word was {rand_word}.")

        play = check_input_lab3.get_yes_no("Do you wonna play agian? (Y/N): ")

if __name__ == "__main__":
    main()
