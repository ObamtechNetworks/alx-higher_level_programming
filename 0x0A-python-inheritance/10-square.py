#!/usr/bin/python3
"""This module defines an empty class: base geometry
This would serve as the base class for next coming classes
added area instance method
added int validato
added a subclass rectange
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass of Rectangle which is a subclass of BaseGeometry"""
    def __init__(self, size):
        """initialzie square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
