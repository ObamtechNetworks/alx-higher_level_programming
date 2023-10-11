#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Egde cases, for empty matrix
    if not matrix:
        return []  # return an empty matrix

    # case for 1D array
    if isinstance(matrix[0], int):  # case for 1D array
        new_matrix = []  # start an empty list
        for x in matrix:
            if isinstance(x, int):  # check if individual el is an int
                new_matrix.append([x ** 2])
            else:
                pass
                # raise ValueError("invalid element")
        return new_matrix  # return new array
    # case for 2D array
    elif all(isinstance(row, list) for row in matrix):
        new_matrix_row = []  # init. an empty outer matrix
        for row in matrix:
            squared = []
            for x in row:
                if isinstance(x, int):
                    squared.append(x ** 2)
                else:
                    pass
                    # raise ValueError("invalid element")
            new_matrix_row.append(squared)
        return new_matrix_row
    else:
        raise ValueError("invalid input")
