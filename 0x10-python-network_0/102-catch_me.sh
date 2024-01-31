#!/bin/bash
# sends request to 0.0.0.0:5000/catch_mee
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
