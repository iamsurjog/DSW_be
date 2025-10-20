import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

def query(query: str):
    cursor.execute(query)
    if "select" in query.casefold():
        return cursor.fetchall()

conn.commit()



