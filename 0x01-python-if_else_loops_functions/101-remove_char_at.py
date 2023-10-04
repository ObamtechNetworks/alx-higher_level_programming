#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []  # initialize an empty list to convert string literal
    for c in str:  # iterate str literal & append chars into new_str list
        new_str.append(c)
    try:  # while check for error, use the pop rm item of index from list
        new_str.pop(n)
        new_str = ''.join(new_str)  # convert list to string
    except IndexError:  # error exeception
        new_str = str  # former string to new_str
    return new_str  # return new string
