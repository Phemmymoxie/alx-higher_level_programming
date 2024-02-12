#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """ an empty class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        add = 2 * (self.__width + self.__height)
        return add

    def __str__(self):
        resp_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            if i != self.__height - 1:
                resp_str += "#" * self.__width + "\n"
            else:
                resp_str += "#" * self.__width
        return resp_str
