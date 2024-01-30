#!/usr/bin/python3
"""
A script that takes in a URL send request
and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import urllib.error as Error
import sys


# create funtion for clean code
def handle_error(url):
    """
    Sends a request to a URL and displays
    the  body of the response
    decoded in utf-8
    Args:
    (url): (str) --> the url to open
    """
    # prepare url for request
    req = urllib.request.Request(url)

    try:
        # send the POST request and handle the response
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Error.HTTPError as e:
        print(f"Error code: {e.status}")


if __name__ == "__main__":
    handle_error(sys.argv[1])
