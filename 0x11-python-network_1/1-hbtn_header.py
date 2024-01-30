#!/usr/bin/python3
"""A script that sends request to a URL
Also displays the value of the X-Request-Id found in the
header of the response
"""

import urllib.request
import sys


# create funtion for clean code
def fetch_header(url):
    """
    Sends a request to a URL and displays
    the  value of the X-Request-Id variable found
    in the header of the response
    Args: url -> str --> the url to open
    """
    # open the given url
    try:
        with urllib.request.urlopen(url) as response:
            # get the X-Request-Id from the headers
            html_id = response.getheader("X-Request-Id")
            print(html_id)
    except Exception as e:
        pass


if __name__ == "__main__":
    fetch_header(sys.argv[1])
