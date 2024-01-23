#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None

    new_list = sorted(my_list)
    return new_list[list_len - 1]
