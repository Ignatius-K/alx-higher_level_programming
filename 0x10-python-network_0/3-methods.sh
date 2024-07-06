#!/bin/bash
# Script makes OPTIONS request for allowed methods
curl -sI -X OPTIONS $1 | grep -i "Allow" | cut -d " " -f 2-
