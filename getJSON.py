import urllib.request, json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
       data = json.loads(operUrl.read())
    else:
       print("Error receiving data", operUrl.getcode())
    return data
