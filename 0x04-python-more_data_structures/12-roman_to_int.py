#!/usr/bin/python3
def roman_to_int(roman_string):
    # edge case if arg is not a string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # create a dictionary of basic int values for basic roman numberals
    numerals = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
            }
    # normalize given string convert to uppercase
    roman_string.upper()
    # start number at 0
    number = 0
    # store a prev value and start at 0
    prev = 0
    # loop through string in reverse and dict to do conversion
    for c in reversed(roman_string):  # e.g IX => XI
        if c in numerals:
            cur_val = numerals[c]  # 10 as first frm str above
            if cur_val < prev:  # this is false
                number -= cur_val
            else:
                number += cur_val  # number is 10
            prev = cur_val  # prev stores 10
        else:
            return 0  # invalid characters in str
    # return the converted number
    return number
