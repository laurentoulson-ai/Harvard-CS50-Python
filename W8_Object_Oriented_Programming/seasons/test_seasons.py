"""
TASK: Test functionality of seasons.py
"""
import pytest
from datetime import date, timedelta
from seasons import days_since_birth, convert_to_mins, mins_to_words, main

# Test days_since_birth()
def test_days_since_birth():
    # Test normal case
    test_today = date(2000, 1, 1)
    assert days_since_birth("1999-01-01", today=test_today) == 365

    # Test leap year
    test_today = date(2000, 3, 1)
    assert days_since_birth("2000-02-28", today=test_today) == 2

    # Test future date
    assert days_since_birth("3000-01-01") == "Error: Date of birth cannot be in the future."

    # Test invalid format
    assert days_since_birth("January 1, 1999") == "Invalid date format. Please use YYYY-MM-DD."

# Test convert_to_mins()
def test_convert_to_mins():
    assert convert_to_mins(1) == 1440
    assert convert_to_mins(365) == 525600
    assert convert_to_mins(0) == 0
    assert convert_to_mins(10000) == 14400000

# Test mins_to_words()
def test_mins_to_words():
    assert mins_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert mins_to_words(1051200) == "One million, fifty-one thousand, two hundred"
    assert mins_to_words(0) == "Zero"
    assert mins_to_words(1440) == "One thousand, four hundred forty"

# Test edge cases
def test_edge_cases():
    # Test minimum valid date
    assert days_since_birth("0001-01-01") > 0

    # Test today's date
    today = date.today()
    assert days_since_birth(today.isoformat()) == 0

    # Test large numbers
    assert "million" in mins_to_words(2000000)
    assert "billion" in mins_to_words(2000000000)

# Test with specific today dates
def test_with_specific_today():
    test_today = date(2003, 1, 1)
    days = days_since_birth("2001-01-01", today=test_today)
    assert days == 730
    assert mins_to_words(convert_to_mins(days)) == "One million, fifty-one thousand, two hundred"
