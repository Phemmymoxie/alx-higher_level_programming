#!/usr/bin/python3

def uniq_add(my_list=[]):
    sort_list = []
    result = 0
    for i in range(len(my_list)):
        if my_list[i] not in sort_list:
            sort_list.append(my_list[i])
    for i in range(len(sort_list)):
        result += sort_list[i]

    return result
