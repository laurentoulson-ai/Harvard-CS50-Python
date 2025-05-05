# Prompt user for fraction in format X/Y
# X and Y are integers
# Output as a percentage rounded to the nearest integer, how much fuel is in the tank. (i.e. 25%)
# If < 1% output E
# If > 99% output F
# Continue prompting user if:
#   X is greater than Y
#   X or Y are not integers
#   Y is 0

while True:
    try:
        # splits strings into into two separate variables
        numerator_str, denominator_str = input("Fraction: ").split('/')

        # converts strings to integers
        numerator = int(numerator_str)
        denominator = int(denominator_str)

        # Checks if Y is 0 then raises ZeroDivisionError
        if denominator == 0:
            raise ZeroDivisionError

        # Checks that X is not greater than Y
        if numerator > denominator:
            raise ValueError

        # calculate percentage and round it so no float at end
        remaining_fuel = round((numerator / denominator) * 100)

        # handles special cases
        if remaining_fuel <= 1:
            print("E")
        elif remaining_fuel >= 99:
            print("F")

        # otherwise prints percentage
        else:
            print(f"{remaining_fuel}%")

        # exit the loop only if input was valid
        break

    except ValueError:
        print("Invalid input. Please enter a fraction (e.g., 1/2).")
    except ZeroDivisionError:
        print("Denominator cannot be zero. Try again.")
