#!/usr/bin/python3

"""Script makes request to URL and display value of Response Header"""

import sys
import urllib.request

if __name__ == "__main__":
    REQUIRED_HEADER = "X-Request-Id"
    URL = sys.argv[1]

    with urllib.request.urlopen(URL) as response:
        print(response.getheader(REQUIRED_HEADER))
