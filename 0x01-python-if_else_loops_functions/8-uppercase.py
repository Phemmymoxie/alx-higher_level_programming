#!/usr/bin/python3

def uppercase(str):
    for char in str:
        chk = ord(char)
        if 96 < chk < 122:
            chk -= 32
            print("{}".format(chr(chk)), end='')
        else:
            print(char)
