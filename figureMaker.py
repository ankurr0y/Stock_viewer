import matplotlib.pyplot as plt
import matplotlib

def getBar(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed):
    plt.bar(date_x,statistic_y)
    fileName=company+fromDate+toDate+chartType+statUsed+'.png'
    plt.savefig('Charts/'+fileName)
    return(fileName)

def getScatter(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed):
    plt.scatter(date_x,statistic_y,c='red')
    fileName=company+fromDate+toDate+chartType+statUsed+'.png'
    plt.savefig('Charts/'+fileName)
    return(fileName)

def getPlot(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed):
    plt.plot(date_x,statistic_y,c='red')
    fileName=company+fromDate+toDate+chartType+statUsed+'.png'
    plt.savefig('Charts/'+fileName)
    return(fileName)

def getAll(date_x,statistic_y,company,fromDate,toDate,chartType,statUsed):
    plt.bar(date_x,statistic_y)
    plt.scatter(date_x,statistic_y,c='red')
    plt.plot(date_x,statistic_y,c='green')
    fileName=company+fromDate+toDate+chartType+statUsed+'.png'
    plt.savefig('Charts/'+fileName)
    return(fileName)
