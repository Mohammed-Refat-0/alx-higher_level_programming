#!/bin/bash
# output byte size of HTTP body response for a given URL.
curl -s -X GET "$1" | wc -c
