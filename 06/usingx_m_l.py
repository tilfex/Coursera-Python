import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1252291.xml'
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
sumnum = 0
lstcount = list()
for comment in lst:
    count = comment.find('count').text
    lstcount.append(int(count))
for num in lstcount:
    sumnum = sumnum + num
print(sumnum)