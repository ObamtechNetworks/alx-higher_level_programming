#!/bin/bash
# a script that sends a request to a URL and displays response

# Check if a URL was passed as an argument
if [ -z "$1" ]
then
    echo "No URL provided. Please provide a URL as an argument."
    exit 1
fi

# Send a GET request to the URL and print only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
