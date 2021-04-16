import sqlite3
from datetime import date
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
date1=date(2011,7,3)
table_Datas=[]
conn=sqlite3.connect('Database/'+str(date1)+'.db')
for j in range(1,12):
    url = "http://www.nepalstock.com/main/todays_price/index/"+str(j)+"/?startDate="+str(date1)
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
d = []
for l in range(1, len(level1)):
    q = level1[l].split("\n")
    d.append(q)
df = pd.DataFrame(d[1:],columns=d[0])
df.rename(columns={'Traded Companies': 'company_name','No. Of Transaction': 'no_of_transaction', 'Max Price':'max_price','Min Price':'min_price','Closing Price':'closing_price','Traded Shares':'traded_shares','Previous Closing':'previous_closing','Difference Rs.':'difference_rs'}, inplace=True)
jsn = json.loads(df.to_json(orient='records'))
#print(type(jsn))
for i in range(0,4):
    del jsn[20]
conn.execute("CREATE TABLE STOCKS (COMPANY_NAME CHAR(10000), NO_OF_TRANSACTIONS CHAR(100), MAX_PRICE CHAR(100), MIN_PRICE CHAR(100), CLOSING_PRICE CHAR(100), TRADED_SHARES CHAR(100), PREVIOUS_CLOSING CHAR(100), DIFFERENCE_RS CHAR(100));")
'''for i in range(0,len(jsn)-1):
    if(jsn[i]['company_name']==None):
        del jsn[i]'''
for i in range(0,len(jsn)-1):
    cn=""
    #for j in str(jsn[i]['company_name']):
        #cn=cn+j
    for j in (str(jsn[i]['company_name'])):
        cn=cn+j
    #print(type(cn))
    #print(cn)
    if cn=="None":
        continue
    nt=str(jsn[i]['no_of_transaction'])
    mxp=str(jsn[i]['max_price'])
    mnp=str(jsn[i]['min_price'])
    cp=str(jsn[i]['closing_price'])
    ts=str(jsn[i]['traded_shares'])
    pc=str(jsn[i]['previous_closing'])
    dr=str(jsn[i]['difference_rs'])
    conn.execute("INSERT INTO STOCKS(COMPANY_NAME, NO_OF_TRANSACTIONS, MAX_PRICE, MIN_PRICE, CLOSING_PRICE, TRADED_SHARES, PREVIOUS_CLOSING, DIFFERENCE_RS) VALUES ('"+str(cn)+"', "+nt+", "+mxp+", "+mnp+", "+cp+", "+ts+", "+pc+", "+dr+")")
    conn.commit()
conn.close()
