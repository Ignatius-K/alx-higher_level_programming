#!/usr/bin/python3

"""Script that make request URL with an email"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    request_url = sys.argv[1]
    email = sys.argv[2]

    data = {
        'email': email
    }
    payload = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request(request_url, data=payload)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
