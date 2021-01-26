import requests

ticket = input()

r = requests.get("http://192.168.1.178:4567/check?ticket=" + ticket)
print(r.json()['status'])
print(r.json()['message'])