#!/usr/bin/python3

"""Script makes HTTP-POST request with parameter"""

import sys
import requests
from requests import Request, Session, exceptions

if __name__ == "__main__":
    query_param = sys.argv[1] if len(sys.argv) > 1 else ""
    request_url = "http://0.0.0.0:5000/search_user"

    request = Request(
        method="post",
        url=request_url,
        data={
            "q": query_param
        }
    )

    session = Session()
    prepared_request = request.prepare()

    try:
        response = session.send(prepared_request)
        response_body = response.json()
        if (len(response_body.keys()) == 0):
            print("No result")
        else:
            print(f"[{response_body.get("id")}] {response_body.get("name")}")
    except requests.JSONDecodeError:
        print("Not a valid JSON")
