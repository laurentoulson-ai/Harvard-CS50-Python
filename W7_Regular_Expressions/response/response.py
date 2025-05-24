"""
Task: Using validators, prompt user for email address and return valid or invalid
"""
from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    """ Using validate library present checker for email addresse """
    if checkers.is_email(email) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
