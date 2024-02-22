#!/usr/bin/python3
""" add attribute to a class """


def add_attribute(obj, att, value):
    """ add_attribute function """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
