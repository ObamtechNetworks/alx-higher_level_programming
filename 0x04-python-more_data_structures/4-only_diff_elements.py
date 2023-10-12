#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # if an empty set is given or None or invalid set
    if set_1 is None or set_2 is None or not set_1 or not set_2:
        return set()
    # if given input is not a set
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return set()

    # get difference of sets
    diff1 = set_1 - set_2
    diff2 = set_2 - set_1
    # combine difference
    comb_diff = diff1.union(diff2)
    return comb_diff  # elem. in a or b but not both
