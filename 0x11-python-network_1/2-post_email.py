#!/usr/bin/python3
"""
A script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys


# create funtion for clean code
def post_email(url, email):
    """
    Sends a POST request to a URL and displays
    the  body of the response
    decoded in utf-8
    Args:
    (url): (str) --> the url to open
    (msg): (str) --> the message request to send
    """
    # prepare data for the POST request
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    # create the POST request
    req = urllib.request.Request(url, data)

    try:
        # send the POST request and handle the response

        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Exception as e:
        pass


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
