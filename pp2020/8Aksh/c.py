words = list(map(lambda a: a.lower(), list(map(str, input().split()))))
cnt = 0

for i in words:
    if i == 'almaty':
        cnt += 1

print(cnt)