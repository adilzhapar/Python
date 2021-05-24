h, a, b = map(int, input().split())
cnt = 0
x = 0

while x <= h:
    if x + a >= h:
        cnt += 1
        break
    else:
        x = x + a - b
    cnt += 1
print(cnt)