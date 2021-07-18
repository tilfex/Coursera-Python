import urllib.request, urllib.parse, urllib.error
import json

api_key = 42
address = 'Virginia Commonwealth University'
dataforapi = dict()
dataforapi['address'] = address
dataforapi['key'] = api_key
urltoapi = 'http://py4e-data.dr-chuck.net/json?'
url = urltoapi + urllib.parse.urlencode(dataforapi)
#print(url)

openurl = urllib.request.urlopen(url)
readurl = openurl.read().decode()
js = json.loads(readurl)
#print(js)
lst = list()
results = js['results'][0]['place_id']
print('place_id', results)