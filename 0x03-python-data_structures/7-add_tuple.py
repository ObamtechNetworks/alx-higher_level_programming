#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # edge cases if tuples are empty
    if len(tuple_a) == 0 and len(tuple_b) != 0:
        return (tuple_b)
    elif len(tuple_b) == 0 and len(tuple_a) != 0:
        return (tuple_a)
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    list_a = list(tuple_a)[:2]  # Transform the tuples to a list
    list_b = list(tuple_b)[:2]  # with only first two elements
    list_add = []  # create an empty list for the addition
    # if length == 1
    if len(list_a) < 2:
        list_a.append(0)
    elif len(list_b) < 2:
        list_b.append(0)
    # since it's just list of len 2, we can just access index directly
    list_add = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    new_tuple = tuple(list_add)  # CONVERT THE NEW LIST TO TUPLE
    return new_tuple  # return the new tuple
