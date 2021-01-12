import requests

request = requests.get("https://ya.ru")

print(request.content)