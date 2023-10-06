#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # reverse the list using the reverse method
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
