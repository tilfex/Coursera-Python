import re
filehandle = open('regex_sum_1252287.txt')
calcsum = 0
for line in filehandle:
    if len(re.findall('[0-9]+', line))>0:
        x = re.findall('[0-9]+', line)
        for num in x:
            calcsum = calcsum + int(num)
print(calcsum)

