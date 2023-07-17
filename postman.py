import requests

req = requests.post('http://127.0.0.1:8000/', json={'type': 'wall_post_new'})
print(req.text)