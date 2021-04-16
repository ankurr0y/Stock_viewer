import sqlite3

conn=sqlite3.connect("Database/2021-03-23.db")
cursor = conn.execute("SELECT * from STOCKS")
for row in cursor:
    print(row)
