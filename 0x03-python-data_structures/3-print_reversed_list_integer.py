#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # what if list is empty?
    if my_list is None:
        return None

    # reverse the list using the reverse method
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
