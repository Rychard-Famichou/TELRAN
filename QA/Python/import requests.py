import requests
import unittest
import json
body = '{"id": 4512, "category": {"id": 1, "name": "good"}, "name": "good", "photoUrls": ["good"],"tags": [{"id": 1, "name": "good"}], "status": "good"}'
body_json = json.loads(body)
r = requests.post('https://petstore.swagger.io/v2/pet', json=body_json)
print(r.status_code)
r = requests.get('https://petstore.swagger.io/v2/pet/4512')
print(r.status_code)
r = requests.delete('https://petstore.swagger.io/v2/pet/4512')
print(r.status_code)