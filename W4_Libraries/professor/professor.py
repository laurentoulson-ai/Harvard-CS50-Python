# TASK
# prompts user to attempt to solve 10 addition problems, 3 times each, printing EEE if incorrect each time
# on 3rd attempt, prints answer if incorrect 3 times, and moves to next question
# output score out of 10

import random

def main():

    questions_remaining = 10  # count for 10 addition problems (X + Y =)
    score = 0  # Track correct answers
    level = (get_level())
    # Get user's level (1, 2, or 3) outside of loops so input not asked multiple times

    while questions_remaining > 0:
        # generate the random numbers using my functions
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y  # tells it that the correct answer is whatever x + y is
        attempts_left = 3  # allows for 3 attempts per question

        while attempts_left > 0:
            try:
                user_answer = int(
                    input(f"{x} + {y} = "))
                    # x and y uses the random numbers generated each time in generate_integer
                if user_answer == answer:
                    print("Correct!")
                    questions_remaining -= 1  # deducts from questions counter
                    score += 1  # starts counting their score / 10
                    break  # Exit attempts_left loop, moves to next question
                else:
                    attempts_left -= 1
                    print("EEE")
            except ValueError:
                attempts_left -= 1
                print("EEE")  # Handle non-integer inputs

        if attempts_left == 0:
            print(f"Answer: {x} + {y} = {answer}")
            questions_remaining -= 1  # Counts failed answer as 1 of the 10 questions

    print(score)  # outputs final score at end of programme


def get_level():
    # prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3

    while True:
        try:
            user_level = int(input("Level: "))
            valid_levels = [1, 2, 3]  # store valid levels in list

            for levels in valid_levels:
                if user_level == levels:  # checks if user inputted valid level
                    return user_level

        except:
            print("Invalid level")  # to catch rogue inputs like cat


def generate_integer(level):
    # 'level' here is stored in main, where I make get_level = 'level'
    # returns a randomly generated non-negative integer with 'level' digits or raises a ValueError if level is not 1, 2, or 3

    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")

    if level == 1:
        return random.randint(0, 9)  # 1-digit (0-9)
    elif level == 2:
        return random.randint(10, 99)  # 2-digit (10-99)
    elif level == 3:
        return random.randint(100, 999)  # 3-digit (100-999)


if __name__ == "__main__":
    main()
