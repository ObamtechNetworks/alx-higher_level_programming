#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # loop through the outer and inner list
    for items in matrix:
        for i in items:
            if items.index(i) != (len(items) - 1):
                print("{}".format(i), end=' ')
            else:
                print("{}".format(i), end='')
        print()
