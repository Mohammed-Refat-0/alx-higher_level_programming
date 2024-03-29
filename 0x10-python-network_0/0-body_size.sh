#!/bin/bash
# output byte size of HTTP body response for a given URL.
curl -s "$1" | wc -c
