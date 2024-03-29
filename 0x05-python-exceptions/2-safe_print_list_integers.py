#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                printed += 1
            except ValueError:
                pass
            except TypeError:
                pass
    except IndexError:
        raise
    print()
    return printed
