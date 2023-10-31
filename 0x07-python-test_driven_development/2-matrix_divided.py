#!/usr/bin/python3
"""This module defines a function that divides all elements of a matrix

Sample usage: <arg1> a matrix, <arg2> the divisor, div
Returns: a new matrix with the divided elements
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix

    Args:
        matrix (:obj: list of lists): must be a matrix of equal rows
        div (int, float): must be an integer or float

    Returns:
        returns a new matrix with each element divided by <div>

    """
    # case 1 check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # case 2 check if list is list of lists (matrix)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    # case 3 check if rows of matrix are of equal length
    row_len = len(matrix[0])  # get the len of first row
    for row in matrix:
        if len(row) != row_len:  # check each rows against sample row
            raise TypeError("Each row of the matrix must"
                            " have the same size")

    # case 3 check if all elements of matrix is int or float
    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    # case 5 check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # case 6 check if div == 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # BEGIN COMPUTATIONS IF ALL TESTS PASSED
    result = []

    for row in matrix:
        row_division = []
        for el in row:
            row_division.append(round((el / div), 2))
        result.append(row_division)

    return result
