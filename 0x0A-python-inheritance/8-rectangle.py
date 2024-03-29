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
