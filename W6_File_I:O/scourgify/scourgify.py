# TASK
# Expect user to provide two command-line arguments:
    # the name of an existing CSV file to read as input, whose columns are assumed to be, in order: Last, First,House
    # the name of a new CSV to write as output, whose columns should be, in order: First,Last,House
# Converts input CSV, splitting each name into a first name and last name.

import csv
import sys

def main():
    # exit if too few arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # exit if too many arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # assign name to user input
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # exit if input is not .csv file
    if not input_file.endswith('.csv') or not output_file.endswith('.csv'):
        sys.exit("Not a CSV file")

    try:
        with open(input_file, 'r') as input_file:
            input_reader = csv.DictReader(input_file) # make file more readable using csv functions

            # rewrite file in correct structure
            with open(output_file, 'w', newline='') as output_file:
                fieldnames = ['first', 'last', 'house']

                # use dict functions to make it readable as dictionary
                output_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                output_writer.writeheader()

                for row in input_reader:
                    # split the names of input file into first name and surname
                    surname, firstname = row['name'].split(', ')

                    # Create new dictionary with the reorganised data
                    new_row = {
                        'first': firstname,
                        'last': surname,
                        'house': row['house']
                    }
                    output_writer.writerow(new_row)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
