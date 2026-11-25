import sqlite3


connection = sqlite3.connect("db.sql")

cursor = connection.cursor()

Login_name = input("Nome de login: ")
Password = input("Password: ")

command = "INSERT INTO User (login, password) VALUES (?, ?)"
data = (Login_name, Password)

cursor.execute(command, data)

connection.commit()

connection.close()