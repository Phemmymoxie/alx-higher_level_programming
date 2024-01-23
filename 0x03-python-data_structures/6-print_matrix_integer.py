#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for li in matrix:
            if li:
                len_list = len(li)
                for element in range(len_list):
                    if element == len_list - 1:
                        print("{:d}".format(li[element]))
                    else:
                        print("{:d}".format(li[element]), end=' ')
