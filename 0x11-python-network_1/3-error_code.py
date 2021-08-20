#!/usr/bin/python3
"""Send a request and displays
the body response"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(urllib.request.Request(sys.argv[1])) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
