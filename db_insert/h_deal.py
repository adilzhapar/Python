def Convert(string):
    li = list(string.split(","))
    return li

with open("h_dealer.txt", 'r') as f:
    ll = f.readlines();

ll = map(Convert, ll)
# print(*ll, sep='\n')

f = open('output.txt', 'w')
for i in ll:
    i[1] = i[1][0:len(i[1])-1]
    s = "INSERT INTO has_dealer VALUES ({}, '{}');".format(*i)
    print(s)

