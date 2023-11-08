#!/usr/bin/python3
"""This module defines a func that writes a str in `utf-8`

Returns:
    The number of characters written
"""


def write_file(filename="", text=""):
    """this function writes a text to a file in `UTF-8`
    encoding

    Returns:
        the number of characters written
    """
    # open or create the file to write to using the with statement
    with open(filename, "w", encoding="utf-8") as my_file:
        # save the written file to write in a variable
        lines = my_file.write(text)

    # return the number of lines written
    return lines
