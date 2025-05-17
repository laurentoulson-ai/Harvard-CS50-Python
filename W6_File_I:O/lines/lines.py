# TASK
# Accept exactly 1 command line argument - the name of a python file
# Output the number of lines of code in that programme - excluding comments and blank lines
# Exit via sys.exit if: not exactly 1 cmd line arg, or file does not end in .py

import sys

def main():
    # exits if input is not exactly 1 (in addition to programme name)
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    
    # exits if input is not .py file
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    try:
        with open(filename, 'r') as file:
            # count lines, but stripping blank liines and comment lines
            line_count = sum(1 for line in file if line.strip() and not line.lstrip().startswith('#'))
            print(line_count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
