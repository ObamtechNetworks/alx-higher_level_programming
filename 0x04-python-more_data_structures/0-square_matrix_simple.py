#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Egde cases
    if isinstance(matrix[0], int):  # case for 1D array
        try:
            return [x ** 2 for x in matrix]
        except (TypeError, ValueError):
            return 0  # return zero for invalid case
    elif all(isinstance(row, list) for row in matrix):
        try:
            return [[row[x] ** 2 for x in range(len(matrix))]
                    for row in matrix]
        except (TypeError, ValueError):
            return 0  # return zero for invalid case
    else:
        return 0  # return 0 for empty list
