def Convert(string):
    li = list(string.split(","))
    return li

with open("dealers_data.txt", 'r') as f:
    ll = f.readlines();

ll = map(Convert, ll)
# print(*ll, sep='\n')

f = open('output.txt', 'w')
for i in ll:
    i[3] = i[3][0:len(i[3])-1]
    s = "INSERT INTO Dealers VALUES (DEFAULT, '{}', ('{}', '{}', {}));".format(*i)
    print(s)