#!/usr/bin/python3
""" say_my_name function """


def say_my_name(first_name, last_name=""):
    """ Say My Name Function """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
