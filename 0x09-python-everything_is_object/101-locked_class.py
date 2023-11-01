#!/usr/bin/python3
"""This module defines a class that prevents modification of class
attributes unless it the instance is first_name
"""


class LockedClass:
    """Locks a class and prents modifications
    unless instance attribute is first_name
    """
    __slots__ = 'first_name'
