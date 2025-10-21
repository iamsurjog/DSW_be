def query(cursor, query: str):
    cursor.execute(query)
    if "select" in query.casefold():
        return cursor.fetchall()

def commit(cursor):
    cursor.commit()


