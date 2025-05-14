# TASK
# Reimplement fuel.py from W3, using newly defined functions. Test using test_fuel.py

def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            # try to split the fuel
            numerator, denominator = fraction.split("/")
            # convert into integers
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            # calculate the percentage
            f = new_numerator / new_denominator
            # if less than 1, stop the loop
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    # if percent 1 or less than 1 return E (empty)
    if percentage <= 1:
        return "E"
    # if percent 99 greater than 99 return F (Full)
    if percentage >= 99:
        return "F"
    # other, just the percent
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()

