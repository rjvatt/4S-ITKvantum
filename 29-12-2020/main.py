from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/mark")
def helloMark():
    return "Hello Mark!"

@app.route("/joke")
def getJoke():
    jokeRequest = requests.get("https://api.chucknorris.io/jokes/random")
    answerJson = jokeRequest.json()

    return "<img src=\"" + answerJson['icon_url'] + "\" ><p>" + answerJson['value'] + "</p>"

if __name__ == "__main__":
    app.run(host='192.168.1.178', port=4567)