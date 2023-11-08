#!/usr/bin/python3
"""This module defines a function that appends a str to the end of a file

Returns:
    The number of characters added
"""


def append_write(filename="", text=""):
    """this func appends a string to th end of
    a txt file in utf-8 encoding mode

    if file doesn't exits, it is created
    Returns:
        the number of characters added
    """
    # open or create the file for appending
    with open(filename, "a", encoding="utf-8") as my_file:
        # append (write to end) the characters needed
        lines = my_file.write(text)

    # return the number of characters added
    return (lines)
