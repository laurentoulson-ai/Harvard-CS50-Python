# TASK
# Test plates.py

from plates import is_valid

def test_letters(): # 1) Must start with at least two letters
    assert is_valid("AB1234") == True
    assert is_valid("AB") == True
    assert is_valid("ab123") == True
    assert is_valid("A12345") is False, "Not two letters, should return Invalid"

def test_length(): # 2) Length must be between 2 and 6
    assert is_valid("AB12") == True
    assert is_valid("AB123456") is False, "More than 6, should return Invalid"
    assert is_valid("A") is False, "Less than 2, should return Invalid"

def test_lan(): # 3) No letters after numbers (no "AB12C" or "AB1C3")
    assert is_valid("BA321") == True
    assert is_valid("AB1C3") is False, "Letters after numbers, should return Invalid"
    assert is_valid("VA54U") is False, "Letters after numbers, should return Invalid"

def test_notzero(): # 4) First number (if any) is not '0'
    assert is_valid("FA1234") == True
    assert is_valid("FA0123") is False, "First number is 0, should return Invalid"

def test_punct(): # 5) No periods, spaces, or punctuation marks [" ", ".", "," "!", "?"]
    assert is_valid("GH!123") is False, "Contains punctuation, should return Invalid"
    assert is_valid("?GH123") is False, "Contains punctuation, should return Invalid"
    assert is_valid("GH123,") is False, "Contains punctuation, should return Invalid"

if __name__ == "__main__":
    test_letters()
    test_length()
    test_lan()
