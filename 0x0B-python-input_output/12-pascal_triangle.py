#!/usr/bin/python3
"""module defines a function that returns
a list of lists of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of n
    in a pascal triangle's form
    """
    # validate that n is an integer
    if not isinstance(n, int):
        return []
    # return an empty list if n <= 0
    if n <= 0:
        return []

    # start with a list of lists containing 1 as value
    triangle_lists = [[1]]
    for nums in range(1, n):
        # for subs row calc next row's val using prev row
        prev_row = triangle_lists[-1]
        new_row = [1]  # first ele in first row is always 1

        # calc middle element based on prev row
        for i in range(1, nums):
            new_row.append(prev_row[i - 1] + prev_row[i])

        # last ele in the pascal triangle is always 1
        new_row.append(1)
        # add the new row to the triangle
        triangle_lists.append(new_row)

    return triangle_lists
