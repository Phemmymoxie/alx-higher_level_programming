#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list_cpy = my_list.copy()
    for i in range(len(list_cpy)):
        if list_cpy[i] == search:
            list_cpy[i] = replace

    return list_cpy
