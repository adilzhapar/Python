n = int(input())
cnt = 0
i = 1
while i <= n:
    if str(i) == str(i)[::-1]:
        cnt += 1
        
    i += 1
print(cnt)
