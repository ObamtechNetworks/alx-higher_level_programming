#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # edge cases
    if idx < 0 or idx > len(my_list):
        return (my_list)
    # delete item at given index
    del my_list[idx]
    return (my_list)
