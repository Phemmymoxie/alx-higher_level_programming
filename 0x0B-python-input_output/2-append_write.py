#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """ append_write """
    with open(filename, 'w+', encoding='UTF8') as content:
        written = content.write(text)

    return written
