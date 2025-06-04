"""
TASK: Use date class from datetime module to convert a date of birth (YYYY-MM-DD) and print age in minutes to nearest integer
Exit via sys.exit if the user does not input a date in YYYY-MM-DD format
Ensure that your program will not raise any exceptions.
Assume user was born at midnight and that the current time is midnight
Use datetime.date.today to get today’s date
Test with test_seasons.py
"""
import inflect
import sys
from datetime import date


def main():
    try:
        dob_input = input("Date of Birth: ")
        days = days_since_birth(dob_input)
        if isinstance(days, str):  # Error message returned
            print(days)
            sys.exit(1)
        minutes = convert_to_mins(days)
        words = mins_to_words(minutes)
        print(f"{words} minutes")
    except (ValueError, TypeError):
        sys.exit(1)

# Take user date and todays date and work out how many days between
def days_since_birth(dob_str, today=None):
    try:
        dob = date.fromisoformat(dob_str)
        today = today or date.today() # Use provided today or current date
        delta = today - dob

        # Handles errors
        if delta.days < 0:
            return "Error: Date of birth cannot be in the future."
        return delta.days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Convert days to minutes
def convert_to_mins(days):
    return days * 1440 # 1440 minutes per day

# Convert minutes to words
def mins_to_words(num):
    p = inflect.engine()
    words = p.number_to_words(num, andword="")  # Disable 'and', use commas
    # Add commas
    words = (words.replace(" million ", " million, ")
             .replace(" thousand ", " thousand, "))
    # Capitalize first letter
    return words[0].upper() + words[1:]

if __name__ == "__main__":
    main()
