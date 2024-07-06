#!/usr/bin/python3

"""Script sends Request, displays body while handling errors"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    request_url = sys.argv[1]

    request = urllib.request.Request(request_url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode())
    except HTTPError as e:
        print("Error code:", e.code)
