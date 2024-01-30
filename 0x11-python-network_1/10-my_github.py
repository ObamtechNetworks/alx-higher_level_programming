#!/usr/bin/python3
"""
A script that takes in a letter,  sends a POST request
with the letter as a parameter
using the requests package
"""

import requests
import sys


def get_github_user_id(username, access_token):
    # Define the GitHub API endpoint for user details
    url = "https://api.github.com/user"

    # Set up Basic Authentication with personal access token
    auth = (username, access_token)

    # Send a GET request to retrieve user details
    response = requests.get(url, auth=auth)

    try:
        # Try to parse the response JSON
        json_data = response.json()

        # Check if the JSON is properly formatted
        if isinstance(json_data, dict) and 'id' in json_data:
            # Display the user id
            print(f"{json_data['id']}")
        else:
            print(None)
    except Exception as e:
        print(None)


if __name__ == "__main__":
    # Get the GitHub credentials from command line arguments
    username_arg = sys.argv[1]
    access_token_arg = sys.argv[2]

    # Call the function with the provided credentials
    get_github_user_id(username_arg, access_token_arg)
