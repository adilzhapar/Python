def Convert(string):
    li = list(string.split(","))
    return li

with open("model.txt", 'r') as f:
    ll = f.readlines();

ll = map(Convert, ll)
# print(*ll, sep='\n')

f = open('output.txt', 'w')
for i in ll:
    i[4] = i[4][0:len(i[4])-1]
    s = "INSERT INTO Models VALUES (DEFAULT, '{}', '{}', '{}', '{}', {});".format(*i)
    print(s)