#!/bin/bash
# output byte size of HTTP body response for a given URL.
URL=$1
curl -s -X GET "$URL" | wc -c
