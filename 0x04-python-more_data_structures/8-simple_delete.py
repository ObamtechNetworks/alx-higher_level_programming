#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # edge cases, if arg is not a dict or key is not str
    if not isinstance(a_dictionary, dict) or not isinstance(key, str):
        return None
    # check if given key is in dictionary
    if key in a_dictionary:
        # delete given key in dictionary
        del a_dictionary[key]
        return a_dictionary  # return modified dictionary
    else:
        return a_dictionary  # do nothing and return dictionary
