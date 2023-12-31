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

    def to_json(self):
        """ retrieves a dictionary representation of a
        Student instance"""
        # create an empty student dict attr
        student_dict_attr = {}
        # return dict repre in Student,by calling the class to json func
        for key, value in self.__dict__.items():
            # verify collect required attributes
            if isinstance(value, (list, dict, str, int, bool)):
                student_dict_attr[key] = value

        return student_dict_attr
