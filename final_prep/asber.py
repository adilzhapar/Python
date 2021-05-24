asman = set(map(int, input().split()))
n = int(input())
for i in range(n):
    x = set(map(int, input().split()))
    asman.difference_update(x)
print(*asman)