import db
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()


# db.query(cursor, "Create table emp(name varchar(10), age number(2))")
# db.query(cursor, "insert into emp values ('this', 2)")
# print(db.query(cursor, "Select * from emp"))
# db.query(cursor, "drop table emp")
# conn.commit()

print(db.query(cursor, "select name, password, empid from users where empid=11011"))

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{empid}")
async def read_user(empid: str):
    query = db.query(cursor, "select name, password, empid from users where empid=" + empid)[0]
    return {query}

@app.get("/venue/{name}")
async def read_venue(name: str):
    query = db.query(cursor, "select name, isHall from venue where name=" + name)[0]
    return {query}

@app.get("/ccs/{name}")
async def cc(name: str):
    query = db.query(cursor, "select name, login, password from ccs where name=" + name)[0]
    return {query}

@app.get("/bookings/{booking_id}")
async def read_bookings(booking_id: str):
    query = db.query(cursor, "select * from bookings where booking_id=" + booking_id)[0]
    return {query}

@app.get("/{table}")
async def read_item(table: str):
    print(table)
    query = db.query(cursor, "select * from " + table)
    return {tuple(query)}
