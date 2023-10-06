#!/usr/bin/python3
def max_integer(my_list=[]):
    for num in my_list:
        temp = my_list[num]
        if num > temp:
            return num
        else:
            return temp

