import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price integer NOT NULL)
        ''')
    connection.commit()


def get_all_products():
    users = cursor.execute('''SELECT * FROM Products''')
    connection.commit()
    return users.fetchall()


def add_users(username, email, age, balance=1000):
    cursor.execute('''INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)''',
                   (username, email, age, balance))
    connection.commit()


def is_include(username):
    cursor.execute('''SELECT * FROM Users''')
    users = cursor.fetchall()
    connection.commit()
    return bool(users)


