#!/usr/bin/env python3


import os
import json

print("Content-Type: text/html")
print()
# print(os.environ)
print(json.dumps(dict(os.environ)))

