#!/usr/bin/python3

"""Script makes HTTP request and gets Header value"""

import sys
from requests import Request, Session

HEADER_NAME = "X-Request-Id"

if __name__ == "__main__":
    request_url = sys.argv[1]

    session = Session()
    request = Request(method="GET", url=request_url)
    formatted_request = session.prepare_request(request=request)

    response = session.send(formatted_request)
    print(response.headers.get(HEADER_NAME))
