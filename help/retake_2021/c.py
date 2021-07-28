a = map(int, input().split())
b = map(int, input().split())
t = int(input())

cnt = 0
for i, j in zip(a, b):
    if j - i >= t:
        cnt += 1
print(cnt)