#!/usr/bin/python3
def uniq_add(my_list=[]):
    # do operation if list is not empty
    if len(my_list) > 0:
        # generate a unique version of the list
        unique = set(my_list)
        sums = 0
        # iterate through the list to sum values
        for x in unique:
            sums += x
        return sums
    else:
        pass  # do nothing
