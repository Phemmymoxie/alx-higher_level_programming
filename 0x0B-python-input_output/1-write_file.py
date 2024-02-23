#!/usr/bin/python3
""" Write function """


def write_file(filename="", text=""):
    """ write_file function that writes to a file """
    with open(filename, 'w', encoding='UTF8') as content:
        written = content.write(text)

    return written
