#!/usr/bin/python3
""" MyList class that inherit from list"""


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        print(sorted(self))
