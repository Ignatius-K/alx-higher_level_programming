#!/usr/bin/python3

"""Script that fetches Github user details"""

import sys
from requests import Request, Session, exceptions

if __name__ == "__main__":
    username = sys.argv[1]
    password_or_token = sys.argv[2]

    request = Request(
        method="get",
        url="https://api.github.com/user",
        auth=(username, password_or_token)
    )

    session = Session()
    prepared_request = session.prepare_request(request=request)

    response = session.send(prepared_request)
    if (response.ok):
        print(response.json().get("id"))
    else:
        print(None)
