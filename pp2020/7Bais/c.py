n = int(input())
myset = set(map(int, input().split()))
myiter = iter(myset)
for i in range(len(myset)):
    print(i+1, end=' ')
    print(next(myiter))
