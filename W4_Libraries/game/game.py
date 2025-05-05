# Prompt for a "Level: "
# Pass if less than 1
# randomly generate int between 1 and input
# Prompt user to guess the random choice
# If guess is < new_num output Too small!
# If guess is > new_num output Too large!
# If guess is == new_num output Just right!

import random
import sys


def main():

    level = 0

    # loop until level is valid input, before randomising
    while level < 1:
        try:
            level = int(input("Level: "))
            if level < 1:
                print("Level must be ≥ 1!")
        except ValueError:
            print("Level must be an integer!")

    # now randomise a value between 1 and the user input
    new_num = random.choice(range(1, level + 1))

    while True:
        try:
            guess = int(input("Guess: "))

            if guess < new_num:
                print("Too small!")

            elif guess > new_num:
                print("Too large!")

            else:
                print("Just right!")
                sys.exit()  # break and return functions weren't enough for full exit. Needed sys.exit() to pass programme test

        except ValueError:
            print("Invalid input")


main()
