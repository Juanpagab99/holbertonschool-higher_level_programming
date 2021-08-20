#!/bin/bash
#takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -d "email=hr@holbertonschool.com&I will always be here for PLD" -s "$1"
