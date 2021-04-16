import sqlite3
import os
from datetime import date,datetime
import matplotlib.pyplot as plt

files=sorted(os.listdir('Database'))
x=[]
y=[]
for f in files:
    remove='.db'
    n=""
    conn=sqlite3.connect('Database/'+f)
    #print(f)
    cursor=conn.execute("SELECT * FROM STOCKS")
    for j in str(f):
        if j not in remove:
            n=n+j
    current_date=datetime.strptime(n,'%Y-%m-%d')
    for c in cursor:
        if(c[0]=='ICFC Finance Limited'):
            x.append(current_date)
            y.append(float(c[2]))
        '''if(c[0]=='Unilever Nepal Limited'):
            a.append(current_date)
            b.append(float(c[2]))'''
    #print("Database connected")
    conn.close()
fig, ax=plt.subplots()
#ax.autoscale(enable=True, axis='y')
#ax.autoscale(enable=True, axis='x')
#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
#ax.x_label("Dates")
#ax.y_label("Some stat")
#plt.tick_params(axis='y', which='major', labelsize=14)
#ax.plot(x,y,c='red')
#ax.bar(x,y,alpha=0.4)
ax.bar(x,y)
ax.scatter(x,y,c='green')
ax.plot(x,y,c='red')
#ax.bar(a,b,)
fig.autofmt_xdate()
plt.show()
