#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrx = matrix.copy()
    result = [list(map(lambda i: i ** 2, x)) for x in new_matrx]
    return result
