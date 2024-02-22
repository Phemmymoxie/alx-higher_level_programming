#!/usr/bin/python3
""" My int class that inherit from int """


class MyInt(int):
    """ MyInt class"""

    def __eq__(self, value):
        """ equality """
        return self.real != value

    def __ne__(self, value):
        """ non equality """
        return self.real == value
