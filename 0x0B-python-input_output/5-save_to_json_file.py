#!/usr/bin/python3
"""This module defines a function that writes an obj to a txt file

It uses the JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """saves a json object to a file
    if file does not exist, it is created
    """
    # open the file to save to and write the json to it
    with open(filename, "w") as json_file:
        # write to the file in json format using the json dump methdo
        lines = json.dump(my_obj, json_file)
