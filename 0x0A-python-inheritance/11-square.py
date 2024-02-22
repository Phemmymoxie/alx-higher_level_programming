#!/usr/bin/python3
""" Square class that inherits from the Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        """ string return """
        cl_str = "[square] {:d}/{:d}"\
            .format(self.__size, self.__size)
        return cl_str
