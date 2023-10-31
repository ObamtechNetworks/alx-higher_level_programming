#!/usr/bin/python3
"""
This module defines a function that prints the given names passed ot it

It receives two arguments: <first_name> and <last_name>
The two arguments must be a string, else TypeError exception is raised

prototype: def say_my_name(first_name, last_name=""):
Sample Usage:
    >>> say_my_name("Bamidele", "Michael")
    My name is Bamidele Michael

    --> Can also receive one arg
    >>> say_my_name("Bamidele")
    My name is Bamidele

Returns:
    nothing
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>

    Where: <first name> and <last_name> are the given arguments

    Args:
        first_name (string): must be a string
        last_name (string): must be a string

    Returns:
        nonthing

    """
    # case 1: check if first_name is string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # case 2: check if last_name is string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # case 3: Empty strings, value error
    if len(first_name) == 0 and len(last_name) == 0:
        raise ValueError("first_name and last_name cannot be empty")
    # IF ALL CHECKS PASSED, PRINT THE CORRECT OUTPUT
    # result = "My name is" + " " + first_name + " " + last_name

    print("My name is {} {}".format(first_name, last_name))
