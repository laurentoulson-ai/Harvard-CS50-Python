"""
Task: Count from an input string how many times 'um' is said - standalone, not within another word
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """len counts, findall looks for all 'um', backslash b ensures standalone work, ignores the case """
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
