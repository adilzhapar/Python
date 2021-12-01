def Convert(string):
    li = list(string.split(","))
    return li

with open ('cust_data.txt', 'r') as f:
    ll = f.readlines();

for i in range(len(ll)):
    ll[i] = Convert(ll[i])
# print(*ll, sep='\n')

f = open('output.txt', 'w')
for i in ll:
    i[3] = i[3][0:len(i[3])-1]
    # print(number)
    s = "INSERT INTO Customers VALUES (DEFAULT, ('{0}', '{1}'), '{2}', {3});\n".format(i[0], i[1], i[2], i[3])
    f.write(s)
f.close()