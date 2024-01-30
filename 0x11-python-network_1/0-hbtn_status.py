#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


# create funtion for clean code
def openURL(url):
    """
    To open given urls using urllib.request library
    Args: url -> str --> the url to open
    """
    # open the given url
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()

    # print output based on the response read
    print(f"""    - {type(html)}
    - content: {html}
    - utf8 content: {html.decode('utf-8')}""")


url = "https://alx-intranet.hbtn.io/status"
openURL(url)