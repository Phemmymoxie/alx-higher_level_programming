#!/usr/bin/python3
"""class Square"""


class Square:
    """ a class Square """
    def __init__(self, size=0):
        """ instance of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

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

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        for i in range(0, self._Square__size):
            [print("#", end="") for cnt in range(self._Square__size)]
            print("")
        if self._Square__size == 0:
            print("")