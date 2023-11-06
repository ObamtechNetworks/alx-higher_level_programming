#!/usr/bin/python3
"""This module defines an empty class: "BaseGeometry
This would serve as the base class for next coming classes
added area instance method
"""


class BaseGeometry:
    """The base class for geometry objects
    """
    def area(self):
        """method for implementing area"""
        raise Exception(f"{self.area.__name__}() is not implemented")
