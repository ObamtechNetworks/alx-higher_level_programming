#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Egde cases
    if isinstance(matrix[0], (int, float)):  # case for 1D array
        try:
            return [x ** 2 for x in matrix]
        except (TypeError, ValueError):
            pass
    elif all(isinstance(row, list) for row in matrix):
        try:
            return [[row[x] ** 2 for x in range(len(matrix))]
                    for row in matrix]
        except (TypeError, ValueError):
            pass
    else:
        raise TypeError("Expected a list")
