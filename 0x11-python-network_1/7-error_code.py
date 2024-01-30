#!/usr/bin/python3
"""
A script that takes in a URL, sends a request
and displays the body of the response
using the requests package
"""

import requests
import sys


# create funtion for clean code
def get_status_code(url):
    """
    To open given urls and send POST request
    using the requests package
    Args:
    (url) -> str --> the url to open
    """
    # open the given url
    status = requests.get(url)
    try:
        if status.status_code >= 400:
            print(f"Error code: {status.status_code}")
        else:
            print(status.text)
    except Exception as e:
        pass


if __name__ == "__main__":
    get_status_code(sys.argv[1])
