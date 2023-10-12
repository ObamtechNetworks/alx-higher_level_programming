#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # edge cases, ensure arg is a dictionary
    if not isinstance(a_dictionary, dict):
        return None
    # sort the dictinoary elements by keys
    sorted_dict = dict(sorted(a_dictionary.items()))
    # print the sorted dictionary
    for keys, values in sorted_dict.items():
        print("{}: {}".format(keys, values))
