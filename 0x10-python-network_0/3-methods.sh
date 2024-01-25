#!/bin/bash
# a script that displays all HTTP methods the server will allowt
curl -i -X OPTIONS "$1" | grep -i Allow | cut -d' ' -f2-
