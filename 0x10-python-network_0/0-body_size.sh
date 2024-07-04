#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# And displays the size of the body of the response
curl -o /dev/null -s -w %{size_download} "$1"
