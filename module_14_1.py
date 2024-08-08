import sqlite3

connection = sqlite3.connect(' not_telegram.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
               ''')
for i in range(1, 11):
    cursor.execute('''INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)''',
                   ('User' + str(i), 'example' + str(i) + '@gmail.com', i * 10, 1000))

cursor.execute('''UPDATE Users SET balance = 500 WHERE id % ? = ?''', (2, 1))
for i in range(4, 11, 3):
    cursor.execute('''delete FROM Users WHERE id = ?''', (i,))
cursor.execute('''SELECT username, email, age, balance FROM Users Where age != ?''', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Email: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
