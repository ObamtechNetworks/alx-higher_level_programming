#!/usr/bin/python3
"""This module defines a class that demonstrate the representation
of a square

the square inherits from the rectangle class
"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """a representation of a Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        # set width and height with the same value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes from this method if present"""
        attributes = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }

    def __str__(self):
        """prints str representation of Square"""
        return "[{}] ({}) {}/{} - {}".\
               format(type(self).__name__,
                      self.id, self.x,
                      self.y, self.size)
