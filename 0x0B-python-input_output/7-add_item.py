#!/usr/bin/python3
"""
A script that adds all arg to a Python list, and then save them to a file

It uses the function save_to_json_file from 5-save_to_json_file.py

And also, the load_from_json_file fucn from 6-load_from_json_file.py

The list is saved as a JSON representation in a file named add_item.json

If the file doesn’t exist, it is created

file permissions / exceptions is not managed
"""


# import the sys module for CLI args
import sys
import json  # imports the json module

# save CLI args to a file
cmd_args = sys.argv

# create an empty list that takes in all the command line args
python_list = []

# append all the command line arguments to the list
for args in range(1, len(cmd_args)):
    python_list.append(cmd_args[args])

# print(python_list)  # prints the python list

# store the instructed filename into a label
json_file = "add_item.json"

# import the save_to_json_file() func to save all args to a json file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# import load_from_json_file() func to load all file contend into a json
load_from_json_f = __import__('6-load_from_json_file').load_from_json_file

# save python list to json obj
json_obj = python_list
# call the ``save_to_json_file`` func to save the python list to a json obj
save_to_json_file(json_obj, json_file)

# call the load_from_json_file to read the json file and tranform to pyobj
load_from_json_f(json_file)
