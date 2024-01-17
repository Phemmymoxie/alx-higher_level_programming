#!/usr/bin/python3

def remove_char_at(str, n):
    ret_str = ''
    for ind, i in enumerate(str):
        if n == ind:
            continue
        else:
            ret_str += i
    return ret_str
