#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""

import requests


# create funtion for clean code
def openURL(url):
    """
    To open given urls using urllib.request library
    Args: url -> str --> the url to open
    """
    # open the given url
    html = requests.get(url)
    # print output based on the response read
    print(
            f"Body response:\n\t- type: {type(html.text)}\n\t"
            f"- content: {html.text}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    openURL(url)
