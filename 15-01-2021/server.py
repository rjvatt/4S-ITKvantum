import os.path

from flask import Flask, Response, request, jsonify, render_template
import string
import random
import requests


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

# url_for('static', filename='style.css')

database = []


# Главная страница
@app.route("/")
def index():
    return render_template("/index.html", len=len(database), database=database)


# Создание команды
@app.route('/create_team')
def createTeam():
    answer = dict()
    teamDoesNotExist = True
    teamname = request.args.get('teamname')
    if len(teamname) > 0:
        for team in database:
            if team['name'] == teamname:
                teamDoesNotExist = False
                answer['status'] = "Team name already exist"
                answer['id'] = '-1'
        if teamDoesNotExist:
            answer['status'] = "Ok"
            answer['teamid'] = get_random_string(20)
            newTeam = {
                'name': teamname,
                'id': answer['teamid'],
                'score': 0
            }
            database.append(newTeam)
    else:
        answer['status'] = "Team name is too short"
        answer['id'] = '-1'

    return jsonify(answer)


@app.route('/list_team')
def listTeam():
    return jsonify(database)


@app.route('/add')
def addScore():
    teamId = request.args.get('id')
    score = 0
    teamExist = False
    for team in database:
        if team['id'] == teamId:
            team['score'] += 1
            score = team['score']
            teamExist = True
            break
    answer = {
        'status': 'Team does not exist',
        'score': -1
    }
    if (teamExist):
        answer = {
            'status': 'Ok',
            'score': score
        }

    return jsonify(answer)


@app.route('/remove')
def removeScore():
    teamId = request.args.get('id')
    score = 0
    teamExist = False
    for team in database:
        if team['id'] == teamId:
            team['score'] -= 1
            score = team['score']
            teamExist = True
            break
    answer = {
        'status': 'Team does not exist',
        'score': -1
    }
    if (teamExist):
        answer = {
            'status': 'Ok',
            'score': score
        }

    return jsonify(answer)


if __name__ == "__main__":
    app.run(host='192.168.1.178', port=4567)
