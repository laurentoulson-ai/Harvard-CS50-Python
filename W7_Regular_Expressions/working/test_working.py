"""
TASK: implement three or more functions that collectively test your implementation of convert thoroughly,
each of whose names should begin with test_ so that you can execute your tests with pytest
"""

import pytest
from working import convert

def main():
    test_valid()
    test_edge_cases()
    test_ValueError()

def test_valid():
    # Test standard 12h to 24h conversion
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_edge_cases():
    # Test midnight (12 AM) and noon (12 PM)
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("11:59 PM to 12:00 AM") == "23:59 to 00:00"

def test_ValueError():
    # Test invalid inputs raise ValueError
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")  # Invalid minutes
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Wrong separator
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")  # Wrong format
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")  # Invalid hour

if __name__ == "__main__":
    test_valid()
    test_edge_cases()
    test_ValueError()
