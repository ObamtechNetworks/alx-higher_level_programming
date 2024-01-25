#!/usr/bin/env bash
# a script that takes in a url, sends request to the URL
# and display the size of the body as response

if [ "$#" -ge 1 ]; then
	curl -sI "$1" | grep -i Content-Length | cut -f2 -d' '
fi
