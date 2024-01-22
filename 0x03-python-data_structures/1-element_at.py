#!/usr/bin/python3

def element_at(my_list, idx):
    list_len = len(my_list)

    if idx < 0:
        return None
    if idx > list_len - 1:
        return None
    return my_list[idx]


# my_list = [1, 2, 3, 4, 5]
# idx = 3
# print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
