from flask import Flask
from flask import request
import requests
app = Flask(__name__)

chatHistory = ""

@app.route("/")
def index():

    return chatHistory

#/message?login=value&text=value

@app.route('/message')
def getMessage():
    global chatHistory
    text = request.args.get('text')
    login = request.args.get('login')
    print(login, text)
    chatHistory += login + ": " + text + "<br>"
    return chatHistory

if __name__ == "__main__":
    app.run(host='192.168.1.178', port=4567)