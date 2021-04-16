import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from flask import jsonify
from datetime import datetime
table_Datas=[]
for j in range(1,12):
    id=j
    url = "http://www.nepalstock.com/main/todays_price/index/%s" % id
    gethtml = requests.get(url)
    html=gethtml.text
    bs=BeautifulSoup(html,"lxml")
    table=bs.find('table',{'class':'table'})
    tr=table.findAll('tr')
    for td in tr:
        t_d = td.findAll('td')
        for tD in t_d:
            table_Datas.append(td.text.strip())
level1 = pd.Series(table_Datas).drop_duplicates().tolist()
#print(level1)
level2 = []
'''for k in level1:
    if len(k)>35:
        level2.append(k)
    else:
        pass'''

d = []
for l in range(1, len(level1)):
    c = level1[l].split("\n")
    d.append(c)
#print(d)
df = pd.DataFrame(d[1:],columns=d[0])
#print(df)
df.rename(columns={'Traded Companies': 'company_name','No. Of Transaction': 'no_of_transaction', 'Max Price':'max_price','Min Price':'min_price','Closing Price':'closing_price','Traded Shares':'traded_shares','Previous Closing':'previous_closing','Difference Rs.':'difference_rs'}, inplace=True)
jsn = json.loads(df.to_json(orient='records'))
print(len(jsn))
conn=sqlite3.connect('test.db')
banned="-:. "
dt=str(datetime.now())
new_dt=""
for i in dt:
    if i not in banned:
        new_dt=new_dt+i
print(new_dt)
conn.execute("CREATE TABLE OnDate"+new_dt+
             "(NAME CHAR(100) PRIMARY KEY, NT INT, MP INT)")
for i in range(12,len(jsn)-1):
    print(jsn[i]['company_name'])
    print(jsn[i]['no_of_transaction'])
    print(jsn[i]['max_price'])
    conn.execute("INSERT INTO OnDate"+new_dt+"(NAME,NT,MP) VALUES (' "+str(jsn[i]['company_name'])+" ', '"+str(jsn[i]['no_of_transaction'])+"', '"+str(jsn[i]['max_price'])+"')")

conn.commit()

cursor=conn.execute("SELECT * FROM OnDate"+new_dt)
print(cursor)
conn.close()
