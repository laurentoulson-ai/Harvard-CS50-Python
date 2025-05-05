# Prompt the user to input a value and ensure it strips and lowers so it doens't accept answers with spaces or cases

answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

# Set out what should be printed if user inputs anything except these three options

if answer != "42" and answer != "forty two" and answer != "forty-two":
    print("No")

# Set out what should be printed if the input is correct

else:
    print("Yes")
