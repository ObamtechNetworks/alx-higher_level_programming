#!/usr/bin/python3
"""This module defines a class`MyList` demontrating inheritance

`MyList` a derived class inherits from `list` the superclass
"""


class MyList(list):
    """This class inherits all attr and methods from the native:
    list class in Python
    """
    def print_sorted(self):
        """when called, prints generated list in a sorted way"""
        print(sorted(self))
