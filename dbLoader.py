import sqlite3
from datetime import date,timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
date1=date(2021,4,4)
date2=date(2021,4,10)
day = timedelta(days=1)
counter=0
while(date1<=date2):
    print(date1)
    raw_data=[]
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
                raw_data.append(td.text.strip())

    listed_data = pd.Series(raw_data).drop_duplicates().tolist()
    arrayed_data = []
    for l in range(1, len(listed_data)):
        q = listed_data[l].split("\n")
        arrayed_data.append(q)
    df = pd.DataFrame(arrayed_data[1:],columns=arrayed_data[0])
    df.rename(columns={'Traded Companies': 'company_name','No. Of Transaction': 'no_of_transaction', 'Max Price':'max_price','Min Price':'min_price','Closing Price':'closing_price','Traded Shares':'traded_shares','Previous Closing':'previous_closing','Difference Rs.':'difference_rs'}, inplace=True)
    jsn = json.loads(df.to_json(orient='records'))
    for i in range(0,4):
        del jsn[20]
    conn.execute("CREATE TABLE STOCKS (COMPANY_NAME CHAR(10000), NO_OF_TRANSACTIONS CHAR(100), MAX_PRICE CHAR(100), MIN_PRICE CHAR(100), CLOSING_PRICE CHAR(100), TRADED_SHARES CHAR(100), PREVIOUS_CLOSING CHAR(100), DIFFERENCE_RS CHAR(100));")
    for i in range(0,len(jsn)-1):
        cn=""
        for j in (str(jsn[i]['company_name'])):
            cn=cn+j
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
    if(counter==4):
        date1=date1+3*day
        counter=0
    else:
        date1=date1+day
        counter=counter+1
conn.close()
