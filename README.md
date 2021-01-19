# Репозиторий группы 4С IT-Квантума г. Краснодар

### 22.12.2020 Requests + Public Api

### 29.12.2020  API+Telebot
https://codex.so/python-flask

Запустить сервер на Flask, который: 
- по маршруту /joke выдаёт шутку о Чаке Норрисе
- по маршруту /cat выдаёт картинку кошки 
- по маршруту /custom выдаёт некоторый текст, используя любое public API
https://github.com/public-apis/public-apis

### 12.01.2021 Requests + Flask
- Доделать прошлое ДЗ

### 15.01.2021 Python requests competition
~~~
Адрес API:  
http://192.168.1.178:4567/  
Маршруты:  
/create_team?teamname=name - создание команды с именем name  
/list_team - получение перечня всех команд  
/add?id=TOKEN - добавление очков с токеном TOKEN  
/remove?id=TOKEN - удаление очков команде  
~~~

### 19.01.2021 Python + requests qr example
Работа с SQLAlchemy
1. Установка билиотеки
в командной строке выполнить команду: 
pip install Flask
pip install flask-mysql
2. 
~~~py
import pymysql

db = pymysql.connect("localhost", "username", "password", "database")
cursor = db.cursor()
sql = "SELECT * FROM table"
cursor.execute(sql)
results = cursor.fetchall()

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
~~~


***Полезные материалы:***
1. 11 типов современных баз данных: краткие описания, схемы и примеры БД
https://proglib.io/p/11-tipov-sovremennyh-baz-dannyh-kratkie-opisaniya-shemy-i-primery-bd-2020-01-07
2. SQL за 20 минут
https://proglib.io/p/sql-for-20-minutes
3. Подборка материалов для изучения баз данных и SQL
https://proglib.io/p/sql-digest

4. ООП


~~~SQL
SELECT <какие поля> FROM <название таблицы> [WHERE условие]

~~~





Система, позволяющая посетителю получить билет на мероприятие и пройти по нему.  
Проверяющему - проверить билет.  

Билет - уникальная строка, состоящая из N символов
База данных, которая хранит все выданные билеты 

requests.get
Посетитель - клиенты
- Отправить запрос серверу на получение билета и сохранить билет

requests.get
Проверяющий - клиенты
- Отправить запрос серверу на проверку билета

Сервер Flask
- Выдать билет
    Генерирует билет
    Записывает в БД
    Отправить билет

- Проверить билет
    Проверить билет
    Если он находится в БД, удалить и ответить "ОК"
    Если он не находится в БД, ответить "BAD"








