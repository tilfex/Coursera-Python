import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

linklist = list()

url ='http://py4e-data.dr-chuck.net/known_by_James.html'
for i in range(0,7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    x = soup('a')
    for line in x:
        line = str(line)
        link = re.findall('href="(.+)"', line)
        linklist.append(link[0])
    url = linklist[17]
    linklist = list()
name = re.findall('by_([A-Za-z]+).html', url)
print(name[0])
        
        
        
