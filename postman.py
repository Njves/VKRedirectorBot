import requests

req = requests.post('https://vkredirectorbot.onrender.com/', json={'type': 'confirmation', 'group_id': 216438878})
print(req.text)