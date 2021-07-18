import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1252292.json'
openurl = urllib.request.urlopen(url)
readurl = openurl.read().decode()

js = json.loads(readurl)
#print(js)
comments = js['comments']
#print(comments)
sumcount = 0
for com in comments:
    count = com['count']
    #print(count)
    sumcount = sumcount+count
print(sumcount)