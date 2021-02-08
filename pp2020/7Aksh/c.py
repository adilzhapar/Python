n = int(input())
arr = list(map(int, input().split()))
ss = set(arr)

if len(ss) == len(arr):
    print("YES")
else:
    print("NO")

