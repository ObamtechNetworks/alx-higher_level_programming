#!/usr/bin/python3
"""
A script that fetches send a POST request
to a given url using the requests package
"""

import requests
import sys


# create funtion for clean code
def post_email(url, email):
    """
    To open given urls and send POST request
    using the requests package
    Args:
    (url) -> str --> the url to open
    (email):(str) -> the email to send POST request
    """
    # open the given url
    email_body = requests.post(url, email={'email': email})
    print(email_body.txt)


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
