#!/usr/bin/python3

def print_last_digit(number: int):
    num_str = str(number)
    length = len(num_str)
    print(num_str[length - 1], end='')
    return num_str[length - 1]
