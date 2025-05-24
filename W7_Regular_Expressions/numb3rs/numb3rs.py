"""
Task: implement a function called validate that expects an IPv4 address as input as a str
returns True or False if that input is a valid IPv4 address or not
Format = #.#.#.# Each # should be a number between 0 and 255
Test validate() using test_numb3rs.py
"""

import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)
    if matches:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
