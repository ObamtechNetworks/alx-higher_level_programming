#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # edge cases if arg is not a dict and key is not a str
    if not isinstance(a_dictionary, dict) or not isinstance(key, str):
        return None
    # update dictionary with key value pair
    a_dictionary.update({key: value})
    # return the updated dictionary
    return a_dictionary
