#!/usr/bin/python3
def no_c(my_string):
    # creat an empty string
    new_str = ''
    # iterate through my string and remove any occurence of 'c' or 'C'
    for char in my_string:
        if char == 'c' or char == 'C':
            continue  # skip the chars
        else:
            # concatenate the rest into new_str
            new_str = new_str + char
    # return the new string
    return new_str
