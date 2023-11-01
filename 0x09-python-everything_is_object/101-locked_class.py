#!/usr/bin/python3
"""This module defines a class that prevents modification of class
attributes unless it the instance is first_name
"""


class LockedClass:
    """Locks a class and prents modifications
    unless instance attribute is first_name
    """
    allowed_attributes = {'first_name'}  # defines a set of allowed attr

    def __setattr__(self, name, value):
        """intercepts the behaviour of the __setattr__ method
        it only get's to function properly if the name given
        is in the list of the allowed attributes as defined
        in the Public class attribute (variable)
        """

        if name in LockedClass.allowed_attributes:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"object has no attribute '{name}'")
