#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Matrix Division function """
    msg = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
        'division by zero'
    )
    new_matrix = []
    cnt = [0, 0]
    if not isinstance(matrix, list):
        raise TypeError(msg[0])
    cnt[0] = len(matrix)
    if cnt[0] == 0:
        raise TypeError(msg[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg[0])
        elif len(row) == 0:
            raise TypeError(msg[0])
        else:
            if cnt[1] == 0:
                cnt[1] = len(row)
            elif len(row) != cnt[1]:
                raise TypeError(msg[1])
            for col in row:
                if not isinstance(col, (int, float)):
                    raise TypeError(msg[0])
    if not isinstance(div, (int, float)):
        raise TypeError(msg[2])
    elif div == 0:
        raise ZeroDivisionError(msg[3])
    else:
        for row in matrix:
            new_row = list(map(lambda x: round(x / div, 2), row))
            new_matrix.append(new_row)
        return new_matrix
