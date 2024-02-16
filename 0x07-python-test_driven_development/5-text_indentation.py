#!/usr/bin/python3
""" Text Indentation function """


def text_indentation(text):
    """ text_indentation """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text):
        if text[char] in ".?:":
            if text[char + 1] == " ":
                char += 1
            print("\n")
        else:
            print(text[char], end='')
        char += 1
