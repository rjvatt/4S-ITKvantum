import requests

req = requests.get("https://official-joke-api.appspot.com/random_joke")

#print(req.headers)
json = req.json()

joke = json['setup'] + '\n' + json['punchline']
print(joke)
