#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    # edge cases if tuples are empty
    if len(tuple_a) == 0 and len(tuple_b) != 0:
        return (tuple_b)
    elif len(tuple_b) == 0 and len(tuple_a) != 0:
        return (tuple_a)
    else:
        if len(tuple_a) == 0 and len(tuple_b) == 0:
            return None
    # Transform the tuples to a list
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_add = []  # create an empty list for the addition
    if len(list_a) > 2:  # check if the lengths does not exceed or go below 2
        list_a = list_a[:2]
    if len(list_b) > 2:
        list_b = list_b[:2]
    # if length == 1
    if len(list_a) == 1:
        list_a.append(0)
    if len(list_b) == 1:
        list_b.append(0)
    for i in range(len(list_a)):  # LOOP THROUGH list_a and list_b
        j = i
        while j in range(len(list_b)):
            # append the sum of first element of each list
            list_add.append(list_a[i] + list_b[j])
            break  # break inner loop to move to second element
    new_tuple = tuple(list_add)  # CONVERT THE NEW LIST TO TUPLE
    return new_tuple  # return the new tuple
