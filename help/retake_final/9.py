n = int(input())
start = []
final = []
for i in range(n):
    a = list(map(int, input().split()))
    if len(start) == 0:
        start.append(sorted(a))
        final.append(0)
        a.clear()
    else:
        cnt = 0
        for i in start:
            if i == sorted(a):
                cnt += 1
        final.append(cnt)
        start.append(sorted(a))
        a.clear()
    
print(*final, sep='\n')
