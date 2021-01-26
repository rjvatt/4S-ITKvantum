from flask import Flask, jsonify, request
import random
import string
import sqlite3

# Записать список в файл
# Прочитать список из файла

# write list to file

app = Flask(__name__)

tickets = []

@app.route('/')
def hello():
    return "Добро пожаловать на получение и проверку билетов!"

@app.route('/get')
def get():
    N = 50
    ticket = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(N))
    answer = dict()
    tickets.append(ticket)
    answer['ticket'] = ticket
    answer['status'] = '200'
    print(tickets)
    return jsonify(answer)

@app.route('/check')
def check():
    answer = dict()
    ticket = request.args.get('ticket')
    if ticket in tickets:
        answer['status'] = 200
        answer['message'] = 'Проходите'
        tickets.remove(ticket)
    else:
        answer['status'] = 404
        answer['message'] = 'Ты не пройдёшь!'

    return jsonify(answer)

if __name__ == "__main__":
    app.run(host='192.168.1.178', port=4567)