#!/usr/bin/python3
"""This module defines a class ``MyInt``
that inherits from the native int class
"""


class MyInt(int):
    """This class inherits from the
    native int class

    This class will override the builtin int methods
    for equality check
    """
    def __eq__(self, other):
        """this method overrides equality"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """this method overrides not equal"""
        return not super().__ne__(other)
