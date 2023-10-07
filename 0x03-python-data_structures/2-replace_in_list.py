#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # edge case when idx is neg or idx out of range
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    # else replace index with element
    my_list[idx] = element
    return my_list  # returns modified list
