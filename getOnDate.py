from forEachDate import getForDate
from datetime import date,timedelta

date1=date(2016,1,3)
date2=date(2020,12,25)
day=timedelta(days=1)
c=0
v=0
while(date1<=date2):
    if(date1==date(2016,2,9)):
       c=c+1
       v=v+1
       continue
    z=[]
    z=getForDate(date1)
    print(type(z))
    for i in range(0,len(z)-1):
        print(z[i])
        print("\n")
    if(c==4):
        date1=date1+3*day
        c=0
    else:
        date1=date1+day
        c=c+1
    v=v+1
    print(v)
