#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    add_tuple_a = 0
    add_tuple_b = 0
    if len(tuple_a) < 2 and len(tuple_b) < 2:
        if len(tuple_a) > 0:
            add_tuple_a += tuple_a[0]
        if len(tuple_b) > 0:
            add_tuple_b += tuple_b[0]

    elif len(tuple_a) >= 2 > len(tuple_b):
        if len(tuple_b) > 0:
            add_tuple_a += (tuple_a[0] + tuple_b[0])
        else:
            add_tuple_a += tuple_a[0]
        add_tuple_b += tuple_a[1]

    elif len(tuple_b) >= 2 > len(tuple_a):
        if len(tuple_a) > 0:
            add_tuple_a += (tuple_a[0] + tuple_b[0])
        else:
            add_tuple_a += tuple_b[0]
        add_tuple_b += tuple_b[1]

    else:
        add_tuple_a += (tuple_a[0] + tuple_b[0])
        add_tuple_b += (tuple_a[1] + tuple_b[1])

    return tuple((add_tuple_a, add_tuple_b))
