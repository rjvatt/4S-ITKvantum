import requests

baconRequest = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
baconJson = baconRequest.json()

print(baconJson[0])