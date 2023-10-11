#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Egde cases
    if type(matrix) is list:
        # do work only when list is not empty
        if len(matrix) > 0:
            new_matrix = [
                    [row[x] ** 2 for x in range(len(matrix))]
                    for row in matrix]
            return new_matrix
        else:  # if len is negative or 0, return the original matrix
            return matrix
    else:
        raise TypeError("Expected argument type: 'list'")
