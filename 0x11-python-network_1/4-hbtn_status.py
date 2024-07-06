#!/usr/bin/python3

"""Script that makes HTTP request"""

from requests import Request, Session

if __name__ == "__main__":

    request_url = "https://alx-intranet.hbtn.io/status"
    request = Request(method="GET", url=request_url)

    session = Session()
    prepared_request = session.prepare_request(request)
    response = session.send(request=prepared_request)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
