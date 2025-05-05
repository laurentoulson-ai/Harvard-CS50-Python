# Prompts user to make an input
# Remove A E I O U from the input
# Returns input without vowels as Output: {input}

user_input = input("Input: ")
vowels = [
    "a", "e", "i", "o", "u",
    "A", "E", "I", "O", "U"] # stores vowels in list

for vowel in vowels:
    user_input = user_input.replace(vowel, "")  # removes the vowels

print(user_input.strip(), end="")  # Strips any spaces and /n (new line) once at the end
