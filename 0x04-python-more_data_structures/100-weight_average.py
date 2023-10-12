#!/usr/bin/python3
def weight_average(my_list=[]):
    # Edge case: if the input is not a list or is None, return 0
    if not isinstance(my_list, list) or my_list is None:
        return 0
    # Edge case: if the list is empty, return 0
    if not my_list:
        return 0
    # start weight and score at 0
    score_total = 0
    total_weight = 0
    
    # loop through score
    for score, weight in my_list:
        if isinstance(score, int) and isinstance(weight, int) and weight > 0:
            score_total += score * weight
            total_weight += weight
        else:
            return 0

    if total_weight == 0:
        return 0

    weighted_average = score_total / total_weight
    return weighted_average
