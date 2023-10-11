#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Egde cases
    if type(matrix) is list and len(matrix) > 0:
        new_matrix = []
        try:  # do work only when list is valid and not empty
            new_matrix = [
                    [int(row[x]) ** 2 for x in range(len(matrix))]
                    for row in matrix]
        except (TypeError, ValueError) as e:
            return None
        return new_matrix
    else:
        raise TypeError("Expected argument type: 'list'")
