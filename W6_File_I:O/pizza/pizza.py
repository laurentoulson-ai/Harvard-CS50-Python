# TASK
# expect exactly 1 command line argyment - the name of a csv file
# outputs a table formatted as ASCII art using tabulate "grid" format
# exit via csv exit if: incorrect number command line argyments, file doesn't exist, file isn't csv

import sys
import csv
from tabulate import tabulate

def main():
    # exit if too few arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # exit if too many arguments
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # assign name to user input
    filename = sys.argv[1]

    # exit if input is not .csv file
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")

    try:
        with open(filename, 'r') as file:
            # make csv file into an ASCII grid table
            reader = csv.DictReader(file) # make file more readable using csv functions
            grid = tabulate(reader, headers="keys", tablefmt="grid") # DictReader automatically makes header row into keys
            print(grid)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

