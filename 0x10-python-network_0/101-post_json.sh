#!/bin/bash
# sends a JSON POST request to a url passed as first argumene
curl -sX POST "$1" -H "Content-Type: application/json" -d "@$2"
