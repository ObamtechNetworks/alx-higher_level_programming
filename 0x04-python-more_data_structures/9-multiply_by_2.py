#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # edge case for invalid dict arg
    if not isinstance(a_dictionary, dict):
        return None
    # loop thru dictionary and multiply values by 2 and store to a new dict
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict  # return the new dictionary
