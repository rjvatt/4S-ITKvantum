import sqlite3

import datetime

con = sqlite3.connect('olimpbotic.db')
cur = con.cursor()

cur.execute('CREATE TABLE if not exists olympiads (	id integer PRIMARY KEY AUTOINCREMENT,	name text,	level integer,	start_date datetime,	end_date datetime);')
cur.execute('CREATE TABLE if not exists olymp_subjects (	olymp_id integer,	subject_id integer PRIMARY KEY AUTOINCREMENT);')
cur.execute(
    'CREATE TABLE if not exists subjects (	id integer PRIMARY KEY AUTOINCREMENT,	name varchar);')
cur.execute('CREATE TABLE if not exists users (	user_id varchar,	user_name varchar,	user_surname varchar,	class integer);')
cur.execute('CREATE TABLE if not exists olymp_schedule (	user_id varchar,	olymp_id integer PRIMARY KEY AUTOINCREMENT);')


# list_olymps = [
#     'Олимпиада «Газпром»',
#     'Олимпиада «Высшая проба»',
#     'Олимпиада «Будущие исследователи - будущее науки»',
#     'Межрегиональная олимпиада школьников на базе ведомственных образовательных организаций',
#     'Олимпиада «Наследники Левши»'
# ]

# level = 3

# for olymp in list_olymps:

#      query = 'INSERT INTO olympiads (name, level) VALUES (?, ?);'
#      cur.execute(query, [olymp, level])

# con.commit()

cur.execute("SELECT * FROM subjects")
print(cur.fetchall())

result = cur.execute("SELECT * FROM olympiads")
data = result.fetchall()
print(str(data))

for row in data:
    print(row[1])

con.commit()
# cur.execute("SELECT * FROM list_olimps")
# print (cur.fetchall())

# cur.execute('create table if not exists users(user_id integer not null, user_name text, user_surname text, class integer)')

# con.commit()
