"""
TASK: Implement a class called Jar that 1) Sets the capacity of cookies in the jar, 2) return number of cookies as 🍪
3) deposit cookies to jar, or raise ValueError if exceeds capacity, 4) withdraw cookies from jar unless exceeds amount stored
"""
def main():
    jar = Jar() # must be capitalised
    n = int(input("How many cookies to add? "))
    jar.deposit(n)  # Deposit the cookies
    print(f"Jar now has: {jar}")  # Uses __str__
    print(f"Capacity: {jar.capacity}")


class Jar:
    def __init__(self, capacity=12):
        # initialise methods
        self._capacity = None # placeholder
        self.capacity = capacity # triggers @capacity.setter with default =12
        self._size = 0  # Internal counter for cookies

    def __str__(self):
        # return number of cookies in jar as emojis 🍪
        return '🍪' * self.size

    def deposit(self, n): # takes parameter n as as number of cookies to add
        # add cookies to jar - return ValueError if that would exceed jar capacity
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"Invalid deposit: {n}. Must be a positive integer")
        if self._size + n > self._capacity:
            raise ValueError(f"Invalid deposit: {n}. Exceeds jar capacity: {self._capacity}")
        self._size += n

    def withdraw(self, n): # takes parameter n as as number of cookies to add
        # withdraws cookies from jar - returns ValueError if exceeds cookies in jar
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"Invalid withdraw: {n}. Must be a positive integer")
        if n > self._size:
            raise ValueError("Not enough cookies in jar")
        self._size -= n

    @property # 'gets' from __init__ without need for parenthesis, called by jar.size
    def size(self):
        # returns number of cookies in the jar, initially 0 as set in __init__
        return self._size

    @property # gets capacity as self.capacity
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value): # value = 12
        # initiallises with given capacity and raises ValueError if not a non-negative int
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = value

if __name__ == "__main__":
    main()
