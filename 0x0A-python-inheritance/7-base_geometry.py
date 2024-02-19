#!/usr/bin/python3
""" a base class BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value >= 0:
            raise ValueError("<name> must be greater than 0")
