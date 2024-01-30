#!/usr/bin/python3
"""
A script that takes in a letter,  sends a POST request
with the letter as a parameter
using the requests package
"""

import requests
import sys


# create funtion for clean code
def search_API(search_key=""):
    """
    To open given urls and send POST request
    using the requests package
    Args:
    (url) -> str --> the url to open
    (search_key) (str): parameter to search for
    """
    url = "http://0.0.0.0:5000/search_user"
    # Set up the parameters
    params = {'q': search_key}
    # generate response
    response = requests.post(url, data=params)
    try:
        json_data = response.json()
        if json_data and isinstance(json_data, dict):
            if 'id' in json_data and 'name' in json_data:
                print(f'{[json_data["id"]]} {json_data["name"]}')
            else:
                print("Not a valid JSON")
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_API(sys.argv[1])
    else:
        search_API()
