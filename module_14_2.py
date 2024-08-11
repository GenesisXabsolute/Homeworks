import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''DELETE FROM Users WHERE id = ?''', (6,))
cursor.execute('''SELECT COUNT(*) FROM Users''')
total1 = cursor.fetchone()[0]
cursor.execute('''SELECT COUNT(balance) FROM Users''')
total2 = cursor.fetchone()[0]
cursor.execute('''SELECT AVG(balance) FROM Users''')
total3 = cursor.fetchone()[0]
print(f'Общее количество пользователей: {total1} \n'
      f'Количество зарегистрированных пользователей: {total2} \n'
      f'Средний баланс: {total3}')
connection.commit()
connection.close()
