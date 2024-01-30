#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using the requests library
"""

import requests
import sys


# create funtion for clean code
def openURL(url):
    """
    To open given urls and get the X-Request-Id
    using the requets package
    Args: url -> str --> the url to open
    """
    # open the given url
    html = requests.get(url)
    html_ID = html.headers.get("X-Request-Id")
    print(html_ID)


if __name__ == "__main__":
    openURL(sys.argv[1])
