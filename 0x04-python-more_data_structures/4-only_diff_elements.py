#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # if an empty set is given
    if not set_1 and not set_2 or set_1 is None and set_2 is None:
        return set()
    if set_1 is None and set_2 is not None:
        return set_2
    if set_2 is None and set_1 is not None:
        return set_1
    # if given input is not a set
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return set()
    # get difference of sets
    return set_1 ^ set_2
