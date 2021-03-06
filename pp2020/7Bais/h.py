n, k = map(int, input().split())
test = False
for i in range(n):
    height = max(map(int, input().split()))
    if k <= height:
        test = True
if test == True:
    print("YES")
else:
    print("NO")