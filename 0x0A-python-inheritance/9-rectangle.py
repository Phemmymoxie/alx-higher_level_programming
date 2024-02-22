#!/usr/bin/python3
""" A Rectangle Class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.__height = height
        self.__width = width
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ Rectangle Area """
        print(self.__width * self.__height)

    def __str__(self):
        """ The class str() Method """
        cl_str = str(self.__class__.__name__)
        str_rep = f"[{cl_str}] {str(self.__width)}/{str(self.__height)}"
        return str_rep
