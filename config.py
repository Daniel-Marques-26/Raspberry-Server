import sqlite3


connection = sqlite3.connect("db.sql")

cursor = connection.cursor()

user_table_command = '''
CREATE TABLE IF NOT EXISTS User
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
'''

cursor.execute(user_table_command)

connection.commit()

connection.close()