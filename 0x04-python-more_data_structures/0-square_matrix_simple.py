#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Egde cases
    if isinstance(matrix[0], int):  # case for 1D array
        new_matrix = []
        for x in matrix:
            if isinstance(x, int):
                new_matrix = [x ** 2]
            else:
                raise ValueError("invalid element")
        return new_matrix
    elif all(isinstance(row, list) for row in matrix):
        new_matrix = [[]]
        for row in matrix:
            for x in range(len(matrix)):
                if isinstance(row[x], int):
                    new_matrix = [[row[x] ** 2]]
                else:
                    raise ValueError("invalid element")
        return new_matrix
    else:
        return 0  # return 0 for empty list
