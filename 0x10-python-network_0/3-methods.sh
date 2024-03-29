#!/bin/bash
# display all HTTP methods the server will accept.
curl -sI -X GET "$1" | grep "Allow" | cut -d " " -f 2-
