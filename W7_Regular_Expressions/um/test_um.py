"""
Task: Implement three or more functions to test count from um.py
"""
import pytest
from um import count

def test_um():
    assert count("um") == 1 # standalone um
    assert count("Um, thanks, um...") == 2

def test_not_ums():
    assert count("umbrella") == 0 # um within other words
    assert count("Um, thanks for the album") == 1

def test_special_um():
    assert count("um?") == 1 # um + special characters
    assert count("?um") == 1
    assert count("u?m") == 0
