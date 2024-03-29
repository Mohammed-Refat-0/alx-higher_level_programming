#!/bin/bash
# display the http body response from 200 response
echo $(curl -sL -X GET "$1")
