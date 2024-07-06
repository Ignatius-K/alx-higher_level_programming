#!/usr/bin/python3

"""Script post an email"""

from requests import Request, Session
import sys

if __name__ == "__main__":
    request_url = sys.argv[1]
    email = sys.argv[2]

    request = Request(
        method="post",
        url=request_url,
        data={
            'email': email
        }
    )

    session = Session()
    formatted_request = session.prepare_request(request)
    response = session.send(request=formatted_request)
    print(response.text)
