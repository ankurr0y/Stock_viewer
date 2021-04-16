from getJSON import getResponse
import matplotlib.pyplot as plt
import json

url="https://nepse-data-api.herokuapp.com/data/todaysprice"
#url="http://nepstockapi.herokuapp.com/"
data=getResponse(url)
a=[]
b=[]

print(len(data))
print(data[0])
for z in range(0,len(data)-1):
    a.append(data[z]['companyName'])
    b.append(data[z]['closingPrice'])
#for d in data:
    #print(d)
    #print(d['Close'])
    #print(type(d))
    
    #for v in (d['closingPrice']):
        #b.append(float(v))
    #for v in d['closingPrice']:
        #b.append(v)
fig, ax = plt.subplots()
ax.plot(a,b)
plt.show()

    
plt.close()
