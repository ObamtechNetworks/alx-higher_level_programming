#!/usr/bin/python3
"""This module defines a func that creates an obj from a ``JSON file``
"""


import json


def load_from_json_file(filename):
    """this function creates an object from a JSON file

    it opens the given filename for reading and creates a 
    JSON represnation from it and returns the JSON representation
    """
    # open the file for reading
    with open(filename, 'r') as to_json:
        # load the file into a json object, using the json load method
        # tranform the data to a json object
        json_obj = json.load(to_json)

    # return the created json object
    return json_obj
