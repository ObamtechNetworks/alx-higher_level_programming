#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Edge cases | empty list
    if len(my_list) == 0:
        return False
    # start an empty list
    new_list = []
    # Loop through original list
    for i in range(len(my_list)):
        try:
            if my_list[i] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        except TypeError:
            new_list.append(False)
    return new_list
