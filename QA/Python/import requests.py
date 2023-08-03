import requests
import json
body = '{"id": 1, "category": {"id": 1, "name": "good"}, "name": "good", "photoUrls": ["good"],"tags": [{"id": 1, "name": "good"}], "status": "good"}'
body_json = json.loads(body)
r = requests.post('https://petstore.swagger.io/v2/pet', json=body_json)
print(r.status_code)