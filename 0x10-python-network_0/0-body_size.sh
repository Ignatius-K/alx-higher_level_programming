#!/bin/bash
# Script sends request to `URL` and displays response body size
curl -sI $1 | grep -i "Content-Length" | cut -d " " -f 2
