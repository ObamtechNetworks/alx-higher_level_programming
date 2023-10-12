#!/usr/bin/python3
def number_keys(a_dictionary):
    # edge cases, ensure arg is a dictionary
    if not isinstance(a_dictionary, dict):
        return 0
    count = 0
    for keys in a_dictionary:
        count += 1
    return count
