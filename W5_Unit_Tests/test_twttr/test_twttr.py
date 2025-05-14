# TASK
# Implement one or more functions that collectively test your implementation of shorten thoroughly
# Each of whose names should begin with test_ so that you can execute your tests with: pytest test_twttr.py
# Take care to return, not print, a str in shorten. Only main should call print

from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("testing") == "tstng"
    assert shorten("hEllO!") == "hll!"
    assert shorten("123") == "123"

if __name__ == "__main__":
    main()
