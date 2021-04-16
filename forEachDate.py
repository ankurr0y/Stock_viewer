import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import date

def getForDate(date1):
    table_Datas=[]
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
    for i in range(0,4):
        del jsn[20]
    return(jsn)
    #for i in range(0,len(jsn)-1):
    
        

