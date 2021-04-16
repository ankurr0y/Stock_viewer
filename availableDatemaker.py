import os
import sqlite3
files=sorted(os.listdir('Database'))
to_write=[]
for f in files:
    banned=".db"
    new_string=""
    for j in f:
        if j not in banned:
            new_string=new_string+j
    to_write.append(new_string)
file=open("date_list","w")
for w in to_write:
    file.write(w+"\n")
file.close()
