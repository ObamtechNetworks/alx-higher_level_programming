#!/bin/bash
# a script that takes in a url, sends a GET request to URL and displays the body of the response, only 200 status code response
curl -s -L "$1"
