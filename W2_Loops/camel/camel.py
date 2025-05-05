camelCase = input("camelCase: ")

def split_at_caps(camelCase): # Defines a function to convert camelCase to snake_case
    result = [] # Initializes an empty list to build the output
    for char in camelCase: # char iterates over each character in the input
        if char.isupper() and result:  # isupper returns true if char is uppercase. result ensures no _ before first char
            result.append('_') # Inserts underscore before the uppercase letter
        result.append(char.lower()) # Converts the character to lowercase and add to result
    return ''.join(result) # combines the new list into a string.
    # .join() normally goes after a string like.join() so '' creates an empty string to put result

# Example
print(split_at_caps(camelCase))  # Output: "snake_case_string"
