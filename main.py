import db

db.query("Create table emp(name varchar(10), age number(2))")
db.query("insert into emp values ('this', 2)")
print(db.query("Select * from emp"))
db.query("drop table emp")
