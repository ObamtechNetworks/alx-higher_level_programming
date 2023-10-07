#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # negative index or out of range
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    # delete item at given index
    del my_list[idx]
    return (my_list)
