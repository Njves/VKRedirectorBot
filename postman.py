import requests

req = requests.post('http://127.0.0.1:8000/', json={'type': 'confirmation', 'group_id': 216438878})
print(req.text)