import requests

f = true

while (f):
    login = input("Введите логин: ")
    message = input("Введите текст сообщения: ")
    req = requests.get("http://192.168.1.178:4567/message?login=" + login + "&text=" + message)



