#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError, ValueError):
        return None


def my_div(a, b):
    return a / b
