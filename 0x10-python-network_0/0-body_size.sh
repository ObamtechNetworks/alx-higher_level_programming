#!/bin/bash
# a script that takes in a url, sends request to the URL
curl -sI "$1" | grep -i Content-Length | cut -f2 -d' '
