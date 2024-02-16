#!/usr/bin/python3
""" Print_square """


def print_square(size):
    """ Print Square Function """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
