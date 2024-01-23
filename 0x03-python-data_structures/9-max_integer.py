#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    new_list = sorted(my_list)
    return int(new_list[list_len - 1])
