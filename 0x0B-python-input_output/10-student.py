#!/usr/bin/python3
"""this module defines a class that defines a Student represenation
"""


class Student:
    """A class that representating a student object
    It has a method which retrieves the dictionary repre of itself
    """

    def __init__(self, first_name, last_name, age):
        """initialzies the class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a
        Student instance"""
        # check if attrs is a list of strs
        if isinstance(attrs, list) and\
                all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if
                    hasattr(self, attr)}
        else:
            class_attr = {}
            # if attrs is not a list of strings return only the req attr
            for key, value in self.__dict__.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    class_attr[key] = value
            return class_attr
