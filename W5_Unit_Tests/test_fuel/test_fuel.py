# TASK
# Test fuel.py

import pytest
from fuel import convert
from fuel import gauge

def main():
    test_correct_input()
    test_zero_division()
    test_value()

# test ZeroDivisionError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

# test ValueError
def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')

# test correct input
def test_correct_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"


if __name__ == "__main__":
    main()

