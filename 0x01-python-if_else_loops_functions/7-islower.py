#!/usr/bin/python3

def is_lower(c: str):
    check = ord(c)
    if 97 < check < 112:
        return True
    else:
        return False


print(is_lower('G'))
