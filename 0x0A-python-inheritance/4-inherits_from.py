#!/usr/bin/python3
""" inherits from function """


def inherits_from(obj, a_class):
    """ inherits_from """

    if issubclass(type(obj), a_class)\
            and type(obj) != a_class:
        return True
    else:
        return False
