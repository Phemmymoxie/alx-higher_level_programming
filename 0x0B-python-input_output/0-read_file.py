#!/usr/bin/python3
""" File reading """


def read_file(filename=""):
    """ read file function """
    with open(filename, 'r', encoding='UTF8') as content:
        text_read = content.read()
        print(text_read)

    content.close()
