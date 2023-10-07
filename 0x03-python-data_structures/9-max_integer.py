#!/usr/bin/python3
def max_integer(my_list=[]):
    # try to iterate the list
    for num in my_list:
        if num is None:  # if no items
            return None
        temp = my_list[num]
        if num > temp:
            return num
        else:
            return temp
