import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filehandle = open('mbox.txt')
listoforga = list()
listofmail = list()
listofmailend = list()

for line in filehandle:
    if line.startswith('From:'):
        line = line.split()
        listofmail.append(line[1])
#print(listofmail)
for mail in listofmail:
    mail = str(mail)
    mail = mail.split('@')
    listofmailend.append(mail[1])
#print(listofmailend)
for end in listofmailend:
    end = str(end)
    end = end.split('.')
    listoforga.append(end[0])
#print(listoforga)
for orga in listofmailend:
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orga, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (orga, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ? ', (orga, ))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print (str(row[0]), row[1])

cur.close()