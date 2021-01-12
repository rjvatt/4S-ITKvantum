import requests

req = requests.get("http://192.168.1.178:4567/like")

print(req.content)