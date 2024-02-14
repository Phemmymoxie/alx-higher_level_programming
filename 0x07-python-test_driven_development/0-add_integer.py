#!/usr/bin/python3
""" function that adds two integers """


def add_integer(a, b=98):
    """ Return the sum of a and b """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        a = round(a)
    if isinstance(b, float):
        b = round(b)
    return a + b

