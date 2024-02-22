#!/usr/bin/python3
""" Square class that inherits from the Rectangle class"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ the init method """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)
