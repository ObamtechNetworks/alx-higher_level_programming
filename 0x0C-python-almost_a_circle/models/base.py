#!/usr/bin/python3
"""This module defines the `Base Class` for this project
It is the `base or parent` of all classes in the following tasks
The goal is to manage `id` attribute in all future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """This is the `base` class for the future clases of this project
    it manages id attribute of the future clasess and prevents duplicates
    of same code
    """
    __nb_objects = 0  # tracks number of objects

    def __init__(self, id=None):
        """this is instantiates the class attributes"""
        if id is not None:  # assigns given id if id is not none
            self.id = id
        else:
            Base.__nb_objects += 1  # else increments no of objs
            self.id = Base.__nb_objects  # sets id to be nb objs
