#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for li in matrix:
            len_list = len(li)
            for element in range(len_list):
                if element == len_list - 1:
                    print(li[element])
                else:
                    print(li[element], end=' ')
