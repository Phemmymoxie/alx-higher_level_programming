#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    str(a_dictionary.keys())
    normal = sorted(list(a_dictionary.keys()))
    for i in range(len(normal)):
        print("{}: {}".format(normal[i], a_dictionary[normal[i]]))
