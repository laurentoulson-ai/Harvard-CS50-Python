# Conditions:
# All vanity plates must start with at least two letters
# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end. For example:
# AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# No periods, spaces, or punctuation marks are allowed

# Return true if all conditions met, False if not.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Check 1: len >=2 checks it has at least two and isalpha and :2 checks first two are letters
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Check 2: checks if the length is within min and max characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check 3: No letters after numbers (no "AB12C" or "AB1C3")
    has_number = False
    for char in s:
        if char.isdigit():
            has_number = True
        elif has_number:
            # Letter appears after a number → invalid
            return False

    # Check 4: First number (if any) is not '0'
    for char in s:
        if char.isdigit():      # Find the first digit
            if char == '0':     # If it's '0', invalid
                return False
            break              # Stop after checking the first digit

    # Check 5: No periods, spaces, or punctuation marks
        not_allowed = [" ", ".", "," "!", "?"]
        for char in s:
            if char in not_allowed:
                return False

    # If all checks passed
    return True

main()
