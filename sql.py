import sqlite3

with sqlite3.connect("sample.db") as conn:
    c = conn.cursor()
    c.execute("drop table posts")
    c.execute("create table posts(title TEXT, description TEXT)")
    c.execute('insert into posts values("Good", "I\'m good.")')
    c.execute('insert into posts values("Well", "I\'m well.")')
