# Task: Prompt user for written emoji as input and output the icon like :thumbs_up: = 👍

import emoji

user_input = input("Input: ")

# Convert input into emoji, referring to the emoji dataset
# Needs language="alias" bit to handle edge cases, works for most without but not all
user_output = emoji.emojize(f"{user_input}", language="alias")

# Now print the final emoji
print(user_output)
