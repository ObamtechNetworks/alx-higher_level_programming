#!/bin/bash
# a script that sends a DELETE request to the url passed as th first argumnet
curl -s -X DELETE "$1"
