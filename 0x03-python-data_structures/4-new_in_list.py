#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # edge cases
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    # create a new empty list to copy el of orig list
    copy = []
    # append el of my_list into copy
    for el in my_list:
        copy.append(el)
    # replace the required element based on index
    copy[idx] = element
    return copy
