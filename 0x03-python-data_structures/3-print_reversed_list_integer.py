#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)

    cnt = list_len - 1
    for i in range(list_len):
        print("{:d}".format(my_list[cnt]))
        cnt -= 1


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
