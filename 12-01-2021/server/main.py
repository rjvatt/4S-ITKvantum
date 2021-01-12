from flask import Flask
import requests
app = Flask(__name__)

countOfLikes = 0
countOfDislikes = 0

@app.route("/")
def index():
    global countOfLikes
    global countOfDislikes
    answer = "Количество ❤: " + str(countOfLikes) + '<br>' + 'Количество 💔: ' + str(countOfDislikes)
    return answer

@app.route("/like")
def like():
    global countOfLikes
    countOfLikes += 1
    answer = "like"
    return answer

@app.route("/dislike")
def dislike():
    global countOfDislikes 
    countOfDislikes += 1
    answer = "dislike"
    return answer

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