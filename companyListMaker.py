import os
import sqlite3
files=sorted(os.listdir('Database'))
to_write=[]
for f in files:
    conn=sqlite3.connect('Database/'+f)
    cursor=conn.execute("SELECT * FROM STOCKS")
    for c in cursor:
        if c[0] not in to_write:
            to_write.append(c[0])
    conn.close()
file =open("company_list.txt","w")
for w in to_write:
    file.write(w+"\n")
file.close()
