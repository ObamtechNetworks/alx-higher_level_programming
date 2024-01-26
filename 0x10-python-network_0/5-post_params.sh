#!/bin/bash
# a script that sends a POST request with keyvalues
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
