import sqlite3
from datetime import date,datetime
def getFirst(dates,fromDate):
    count=0
    for date in dates:
        if(date==fromDate):
            break
        count=count+1
    return count
def getLast(dates,toDate):
    count=0
    for date in dates:
        if(date==toDate):
            break
        count=count+1
    return count
def getTransactionSum(company,fromDate,toDate):
    dates=[]
    transactions=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                transactions.append(float(c[1]))
        conn.close
    return(sum(transactions))

def getHighestPrice(company,fromDate,toDate):
    dates=[]
    mp=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                mp.append(float(c[2]))
        conn.close
    return(max(mp))

def getLowestPrice(company,fromDate,toDate):
    dates=[]
    lp=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                lp.append(float(c[3]))
        conn.close
    return(min(lp))

def getAvgPrice(company,fromDate,toDate):
    dates=[]
    avgp=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                avgp.append(float(c[4]))
        conn.close
    return(float(sum(avgp)/len(avgp)))

def getTradeTotal(company,fromDate,toDate):
    dates=[]
    traded_shares=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                traded_shares.append(float(c[5]))
        conn.close
    return(sum(traded_shares))


def getGoneDown(company,fromDate,toDate):
    dates=[]
    gd=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                gd.append(float(c[7]))
        conn.close
    count=0
    for g in gd:
        if(g<0):
            count=count+1
    return(count)

def getGoneUp(company,fromDate,toDate):
    dates=[]
    gu=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                gu.append(float(c[7]))
        conn.close
    count=0
    for g in gu:
        if(g>0):
            count=count+1
    return(count)
def getDays(company,fromDate,toDate):
    dates=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    return(count2-count1)

def getDifference(company,fromDate,toDate):
    dates=[]
    cps=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    count1=getFirst(dates,fromDate)
    count2=getLast(dates,toDate)
    for j in range(count1,count2):
        conn=sqlite3.connect('Database/'+dates[j]+'.db')
        cursor=conn.execute('SELECT * FROM STOCKS')
        current_date=datetime.strptime(dates[j],'%Y-%m-%d')
        for c in cursor:
            if(c[0]==company):
                cps.append(float(c[4]))
        conn.close
    return(cps[len(cps)-1]-cps[0])
