#!/bin/bash
# a script that displays all HTTP methods the server will allowt
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -f2- -d':' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//'
