#!/usr/bin/python3
""" is kind of class function """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
