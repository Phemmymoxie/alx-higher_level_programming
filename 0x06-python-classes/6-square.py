#!/usr/bin/python3
"""class Square"""


class Square:
    """ a class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ instance of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        self._position = position

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._position[1] > 0:
            print("")
        for i in range(0, self._Square__size):
            [print("#", end="") for cnt in range(self._Square__size)]
            [print(" ", end="") for cnt in range(self._position[0])]
            print("")
        if self._Square__size == 0:
            print("")


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")