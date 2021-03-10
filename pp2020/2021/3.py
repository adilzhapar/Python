first = list(map(int, input().split()))
second = list(map(int, input().split()))
k = int(input())
cnt = 0
for i in range(len(first)):
    if first[i] <= k and k <= second[i]:
        cnt += 1
print(cnt)