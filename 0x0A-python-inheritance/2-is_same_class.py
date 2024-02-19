#!/usr/bin/python3
""" is_same_class function """


def is_same_class(obj, a_class):
    """ checks if the object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
