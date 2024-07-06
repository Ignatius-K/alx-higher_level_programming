#!/usr/bin/python3

"""Script that fetches given URL"""

import urllib.request

if __name__ == "__main__":
    URL = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(URL) as response:
        body = response.read()

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
