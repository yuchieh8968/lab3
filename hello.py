#!/usr/bin/env python3


import os
import json

print("Content-Type: application/json")
print()
# print(os.environ)
print(json.dumps(dict(os.environ)))

