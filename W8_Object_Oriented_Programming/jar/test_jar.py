"""
# TASK: Test jar.py with at least 4 functions
"""
from jar import Jar
import pytest


def test_init():
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12  # Default should be 12
    assert jar.size == 0       # Should start empty

    # Test custom capacity
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    # Test invalid capacity
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        Jar(-1)  # Negatives are invalid

    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        Jar("12")  # strings are invalid

def test_str():
    jar = Jar() # default capacity = 12
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    # test correct deposits
    jar = Jar() # default capacity = 12
    jar.deposit(1)
    assert jar.size == 1

    # test multiple deposits
    jar = Jar()
    jar.deposit(2)
    jar.deposit(3)
    assert jar.size == 5

    # test incorrect deposits
    jar = Jar(10) # set jar capacity to 10
    with pytest.raises(ValueError, match=f"Invalid deposit: 11. Exceeds jar capacity: 10"):
        jar.deposit(11)

def test_withdraw():
    # test valid withdraw
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

    # test 1st error type
    jar = Jar()
    with pytest.raises(ValueError, match=f"Invalid withdraw: -2. Must be a positive integer"):
        jar.withdraw(-2)

    # test 2nd error type
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError, match=f"Not enough cookies in jar"):
        jar.withdraw(3)
