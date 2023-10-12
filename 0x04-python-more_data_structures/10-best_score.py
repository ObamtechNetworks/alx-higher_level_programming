#!/usr/bin/python3
def best_score(a_dictionary):
    # edge cases invalid arg, key and val
    if not isinstance(a_dictionary, dict):
        return None
    # start max at neg infinity
    max_score = float('-inf')
    # iterate throught the dictioanry to find highest in val
    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if value > max_score:  # check if current val is higher than max
                max_score = value

    # if no score found return None
    if max_score == float('-inf'):
        return None
    # iterate through the dictionary to return key with highest score
    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if value == max_score:
                return key
