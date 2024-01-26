#!/bin/bash
# a script that displays all HTTP methods the server will allowt
curl -s -i -X OPTIONS "$1" | grep -i Allow | cut -f2- -d' ' | tr -s ' ' | sed 's/[[:space:]]*$//'
