import db
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()


db.query(cursor, "Create table emp(name varchar(10), age number(2))")
db.query(cursor, "insert into emp values ('this', 2)")
print(db.query(cursor, "Select * from emp"))
db.query(cursor, "drop table emp")
conn.commit()
