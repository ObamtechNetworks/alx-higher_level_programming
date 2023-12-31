#!/usr/bin/python3
def common_elements(set_1, set_2):
    # if an empty set is given
    if not set_1 or not set_2:
        return set()  # return an empty set
    # if given input is a set
    if isinstance(set_1, set) and isinstance(set_2, set):
        return set_1 & set_2  # elem in a AND b
    else:
        return set()  # return an empty set
