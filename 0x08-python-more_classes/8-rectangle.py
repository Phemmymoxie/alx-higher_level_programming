#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
                resp_str += str(self.print_symbol) * self.__width + "\n"
            else:
                resp_str += str(self.print_symbol) * self.__width
        return resp_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This is a static method."""
        if not isinstance(rect_1, Rectangle) or not\
                isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect_2.area() == rect_1.area():
            return rect_1

        return rect_2 if rect_2.area() > rect_1.area() else rect_1
