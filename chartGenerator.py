import sqlite3
from datetime import date,datetime
#import matplotlib.pyplot as plt
#import figureMaker as fm
#from plotnine import *
from bokeh.plotting import figure, show
from bokeh.io import export_png
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



def chartGenerator(company,fromDate,toDate,chartType,statUsed):
    dates=[]
    date_x=[]
    statistic_y=[]
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
                date_x.append(current_date)
                if(statUsed=='No. of transactions'):
                    statistic_y.append(float(c[1]))
                if(statUsed=='Max price'):
                    statistic_y.append(float(c[2]))
                if(statUsed=='Min price'):
                    statistic_y.append(float(c[3]))
                if(statUsed=='Closing price'):
                    statistic_y.append(float(c[4]))
                if(statUsed=='Traded share volume'):
                    statistic_y.append(float(c[5]))
                if(statUsed=='Previous closing'):
                    statistic_y.append(float(c[6]))
                if(statUsed=='Difference between closing prices'):
                    statistic_y.append(float(c[7]))
        conn.close()
    fig = figure()
    if(chartType=='Plot'):
        fig.line(date_x,statistic_y,color='red')
    if(chartType=='Scatter'):
        fig.scatter(date_x,statistic_y,color='yellow')
    if(chartType=='Both'):
        fig.line(date_x,statistic_y,color='red')
        fig.scatter(date_x,statistic_y,color='yellow')
    #export_png(fig, filename = "file.png")
    #fileName="file.png"
    #show(fig)
    '''plt.bar(1,3)
    plt.show()
    if(chartType=='Bar'):
        fileName=fm.getBar(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed)
    if(chartType=='Scatter'):
        fileName=fm.getScatter(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed)
    if(chartType=='Plot'):
        fileName=fm.getPlot(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed)
    if(chartType=='All three'):
        fileName=fm.getAll(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed)'''
    return(fig)
