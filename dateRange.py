from datetime import date,timedelta

date1=date(2010,5,9)
date2=date(2011,2,12)

day = timedelta(days=1)
c=0
while date1 <= date2:
    print(date1.strftime('%Y-%m-%d'))
    if(c==4):
        date1=date1 + 3*day
        c=0
    else:
        date1 = date1 + day
        c=c+1
