import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

print(cursor)

cursor.close()

