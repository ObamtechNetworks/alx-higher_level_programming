#!/usr/bin/python3
"""this module defines a funct that appends a given str
after a given string in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that appends to a file
    search for a string and append new string after the search str
    """
    # open the file for reading
    with open(filename, 'r') as file:
        lines = file.readlines()  # reads all lines into a list

    # open the file again for writing
    with open(filename, 'w') as file:
        # search for the lines in the list and write after the match
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
