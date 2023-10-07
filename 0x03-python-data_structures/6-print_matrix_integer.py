#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # what if list is empty?
    # loop through the outer and inner list
    for items in matrix:
        if items:  # if there are valid items
            for i in items:
                if items.index(i) != (len(items) - 1):
                    print("{:d}".format(i), end=' ')
                else:
                    print("{:d}".format(i), end='')
            print()
        else:
            print()
