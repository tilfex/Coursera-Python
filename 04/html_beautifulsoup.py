import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1252289.html').read()
soup = BeautifulSoup(html, 'html.parser')
sumnum = 0 #sum of all numbers
x = soup('span')

for line in x:
    line = str(line)
    numbers = re.findall('[0-9]+', line)
    for num in numbers:
        sumnum = sumnum +int(num)
print(sumnum)