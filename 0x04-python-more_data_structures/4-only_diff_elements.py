#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # if an empty set is given
    if not set_1 or not set_2:
        return set()  # return an empty set
    # if given input is None
    if set_1 is None:
        set_1 = set()
    if set_2 is None:
        set_2 = set()
    # if given input is a set
    if isinstance(set_1, set) and isinstance(set_2, set):
        return (set_1 ^ set_2)  # elem. in a or b but not both
    else:
        return set()  # return an empty set
