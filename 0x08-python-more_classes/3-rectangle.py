#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """ an empty class Rectangle """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    def rectangle(self):
        """ This function does nothing """
        pass

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._height == 0 or self._width == 0:
            return 0
        add = self._width + self._height
        return 2 * add

    def __str__(self):
        resp_str = ""
        if self._height == 0 or self._width == 0:
            return ""
        for i in range(self._height):
            resp_str += "#" * self._width + "\n"
        return resp_str
