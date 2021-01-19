import requests

r = requests.get("http://192.168.1.178:4567/get")
print(r.json()['status'])
print(r.json()['ticket'])
