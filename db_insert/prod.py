from random import *
with open('vins.txt', 'r') as f:
    ll = f.readlines()
dick = dict()
for i in ll:
    if i[9] == 'B' or i[9] == 'R':
        dick[i[0:len(i)-1]] = 1
    else:
        dick[i[0:len(i)-1]] = 2
file = open('output.txt', 'w')

for i in dick:
    # print(i, dick[i], sep=' ')
    year = randrange(2000, 2010)
    month = randrange(1,12)
    day = randrange(1,31)
    s = "'{}-{}-{}'".format(year, month, day)
    que = "INSERT INTO produces VALUES('{}', {}, {});\n".format(i, dick[i], s)
    file.write(que)
file.close()