from flask import Flask,render_template,url_for,flash,request,redirect
from showStockspageForm import InfoForm
import pandas as pd
from chartGenerator import chartGenerator
import matplotlib.pyplot as plt
import matplotlib
from bokeh.plotting import figure, show
from getStats import *
app=Flask(__name__)
app.secret_key = 'development key'

#Renders form
@app.route('/',methods=['GET','POST'])
@app.route('/home/',methods=['GET','POST'])
def homepage():
    form=InfoForm()
    return render_template('showOptions.html',form=form)

#Renders resulting statistics
@app.route('/next/',methods=['GET','POST'])
def resultpage():
    company=''
    fromDate=''
    toDate=''
    chartType=''
    statused=''
    if request.method=='POST':
        a=request.form
        for A,B in a.items():
            if(A=='companies'):
                company=B
            if(A=='fromDate'):
                fromDate=B
            if(A=='toDate'):
                toDate=B
            if(A=='choiceChart'):
                chartType=B
            if(A=='statUsed'):
                statUsed=B
        fig=chartGenerator(company,fromDate,toDate,chartType,statUsed)
    show(fig)
    getd=getDays(company,fromDate,toDate)
    tsum=getTransactionSum(company,fromDate,toDate)
    hip=getHighestPrice(company,fromDate,toDate)
    glp=getLowestPrice(company,fromDate,toDate)
    gap=getAvgPrice(company,fromDate,toDate)
    gtt=getTradeTotal(company,fromDate,toDate)
    ggd=getGoneDown(company,fromDate,toDate)
    ggu=getGoneUp(company,fromDate,toDate)
    gd=getDifference(company,fromDate,toDate)
    return render_template('finalResult.html',company=company,fromDate=fromDate,toDate=toDate,getd=getd,tsum=tsum,hip=hip,glp=glp,gap=gap,gtt=gtt,ggd=ggd,ggu=ggu,gd=gd)
if __name__ == '__main__':
   app.run()
