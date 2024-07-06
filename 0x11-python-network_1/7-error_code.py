#!/usr/bin/python3

"""Script makes HTTP request, displays body while handling errors"""

import sys
from requests import Request, Session, exceptions

if __name__ == "__main__":
    request_url = sys.argv[1]

    request = Request(
        method="get",
        url=request_url
    )
    session = Session()
    prepared_request = session.prepare_request(request)

    try:
        response = session.send(prepared_request)
        response.raise_for_status()
        print(response.text)
    except exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
