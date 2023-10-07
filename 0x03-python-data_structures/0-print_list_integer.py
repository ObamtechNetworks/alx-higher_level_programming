#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # case to check for an empty list
    if my_list is None:
        return None

    # printing individual integers
    for i in my_list:
        print("{:d}".format(i))
