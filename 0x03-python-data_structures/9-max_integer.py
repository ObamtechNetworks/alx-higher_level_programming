#!/usr/bin/python3
def max_integer(my_list=[]):
    # check if list is empty
    i = 0
    if i in my_list is None:
        return None
    # start first value as Max
    Max = my_list[i]
    # Loop through the list and compare cur max
    for num in my_list:
        if num >= Max:  # if cur num is > max, reset max as cur num
            Max = num
    # at the end of iteration, and swap return the max value
    return Max
