#!/bin/bash
# Send a GET request to a given URL with a  custome header variable.
curl -sH -X GET "X-HolbertonSchool-User-Id: 98" "${1}"
