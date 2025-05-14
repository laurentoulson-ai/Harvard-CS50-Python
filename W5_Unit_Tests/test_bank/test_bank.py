# TASK
# Tests bank.py

from bank import value

# testing for a variety of inputs for each value condition (0, 20, 100)
def test_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("HELLO!!") == 0

def test_h():
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("H") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("123") == 100
    assert value("") == 100

if __name__ == "__main__":
    test_hello()
    test_h()
    test_other()
