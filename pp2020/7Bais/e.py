n = int(input())
map = {}
for i in range(n):
    cities = [i for i in input().split()]
    map[cities[0]] = cities[2:]
m = int(input())
res = False
last = []
for i in range(m):
    search = input()
    for country, city in map.items():
        if search in city:
            res = True
            last.append(country)
            break
        else:
            res = False            
    if res == False:
        last.append("Unknown")

print(*last, sep='\n')
            
