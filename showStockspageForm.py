from readFile import rFile,rFileDates
from wtforms import FileField,TextAreaField, SubmitField,SelectField,validators, ValidationError,FloatField,RadioField,SelectMultipleField
from flask_wtf import FlaskForm

#forms for the web page
class InfoForm(FlaskForm):
    companies = SelectField('Companies', choices = rFile())
    fromDate = SelectField('From',choices= rFileDates())
    toDate= SelectField('To',choices= rFileDates())
    statUsed=SelectField('Statistic to use',choices= ['No. of transactions','Max price','Min price','Closing price','Traded share volume','Previous closing','Difference between closing prices'])
    choiceChart=SelectField('Chart Choice',choices = ['Scatter','Plot','Both'])
    
