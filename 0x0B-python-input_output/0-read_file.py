#!/usr/bin/python3
"""This module defines a function
that reads a file passed to the function

it prints the read file to the stdout
"""


def read_file(filename=""):
    """reads a given file and prints to the stdout
    """
    # open the file for reading, using the with keyword
    with open(filename, encoding="utf-8") as file:
        # save the file read to a variable
        lines = file.read()

    # print the read files
    print(lines, end="")
