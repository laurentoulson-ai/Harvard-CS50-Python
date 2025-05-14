# TASK
# Re-implement plates.py from W2

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): # is_valid expects a str as input and returns True if that str meets all requirements and False if it does not

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
        not_allowed = [" ", ".", ",", "!", "?"]
        for char in s:
            if char in not_allowed:
                return False

    # If all checks passed
    return True

if __name__ == "__main__":
    main()
