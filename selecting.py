import sqlite3


connection = sqlite3.connect("db.sql")

cursor = connection.cursor()

command = "SELECT * FROM User WHERE login = ? AND password = ?"
data = (input("Login: "), input("Password: "))

cursor.execute(command, data)

user = cursor.fetchone()

print(user)

connection.commit()

connection.close()