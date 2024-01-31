#!/bin/bash
# a script that sends a request to a URL and displays response
curl -s -o /dev/null -w "%{http_code}" "$1"
