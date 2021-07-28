n = int(input())
d = {}
d['a'] = d['b'] = d['c'] = 0
for i in range(n):
    s = list(map(str, input().split()))
    for ind, el in enumerate(s):
        for ind2, el2 in enumerate(s[ind]):
            if ind == 0 and el2 in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                d['a'] += 1
            elif ind == 1 and el2.lower() in 'aeuio':
                d['b'] += 1
            elif ind == 2 and el2 in '1234567890':
                d['c'] += 1
print(d)