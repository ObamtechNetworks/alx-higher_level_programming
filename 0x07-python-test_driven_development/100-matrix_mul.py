#!/usr/bin/python3
"""This module defines a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """a function that multiplies two matrices
    """
    # m_a not a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # m_b not a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # check if m_a is not a matrix
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    # check if m_b is not a matrix
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # check if m_a or m_b is empty
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    # check if m_b is empty
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    # case 3 check if all elements of matrix is int or float
    for row in m_a:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_a should contain only integers "
                                "or floats")

    for row in m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_b should contain only integers "
                                "or floats")
    # case 4 check if rows of matrix are of equal length
    m_a_row_len = len(m_a[0])  # get the len of first row
    for row in m_a:
        if len(row) != m_a_row_len:  # check each rows against sample row
            raise TypeError("each row of m_a must be of the same size")

    # case 5 check if rows of matrix are of equal length
    m_b_row_len = len(m_b[0])  # get the len of first row
    for row in m_b:
        if len(row) != m_b_row_len:  # check each rows against sample row
            raise TypeError("each row of m_b must be of the same size")

    # check if matrices can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # PERFORM MULTIPLICATION
    result = [
            [
                sum(a*b for a, b in zip(X_row, Y_col))
                for Y_col in zip(*m_b)] for X_row in m_a
            ]

    return result
