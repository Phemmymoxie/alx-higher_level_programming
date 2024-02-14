#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        a = round(a)
    if isinstance(b, float):
        b = round(b)
    return a + b


print(add_integer(0.3, 6))

