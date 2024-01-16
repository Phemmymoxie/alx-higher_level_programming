#!/usr/bin/python3

for i in range(10):
    for i2 in range(i + 1, 10):
        if i == 8 and i2 == 9:
            print("{}{}".format(i, i2))
        else:
            print("{}{}".format(i, i2), end=', ')
