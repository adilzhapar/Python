def Convert(string):
    li = list(string.split(","))
    return li

with open("vecs.txt", 'r') as f:
    ll = f.readlines();

ll = map(Convert, ll)
# print(*ll, sep='\n')

f = open('output.txt', 'w')
for i in ll:
    i[2] = i[2][0:len(i[2])-1]
    s = "INSERT INTO Vehicles VALUES ('{}', '{}', '{}', default);".format(*i)
    print(s)