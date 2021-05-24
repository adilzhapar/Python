n = int(input())
attend = {}

for i in range(n):
    name, date = input().split()
    if name not in attend:
        attend[name] = [date]
    elif name in attend and attend[name] != [date]:
        attend[name].append(date)

for i in attend:
    if len(attend[i]) >= 3:
        attend[i] = '+1'
    else:
        attend[i] = 'NO BONUS'

attend = dict(sorted(attend.items(), key=lambda x: x[0]))
for i, j in zip(attend.keys(), attend.values()):
    print(i, j)
