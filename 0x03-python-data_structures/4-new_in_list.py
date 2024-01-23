#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    my_list_cpy = my_list.copy()
    if idx < 0:
        return my_list_cpy
    if idx > list_len - 1:
        return my_list_cpy
    my_list_cpy[idx] = element
    return my_list_cpy
