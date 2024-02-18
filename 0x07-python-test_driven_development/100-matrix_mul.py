#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b."""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row_1 in m_a:
        if not isinstance(row_1, list):
            raise TypeError("m_a must be a list of lists")

    for row_2 in m_b:
        if not isinstance(row_2, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row_1 in m_a:
        for col in row_1:
            if not isinstance(col, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row_2 in m_b:
        for col in row_2:
            if not isinstance(col, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    length_row = []
    for row in m_a:
        length_row.append(len(row))
    if not all(each == length_row[0] for each in length_row):
        raise TypeError("each row of m_a must be of the same size")

    length_row = []
    for row in m_b:
        length_row.append(len(row))
    if not all(each == length_row[0] for each in length_row):
        raise TypeError("each row of m_b must be of the same size")

    a_cols = len(m_a[0])
    b_rows = len(m_b)
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for i in range(a_cols)] for j in range(b_rows)]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
