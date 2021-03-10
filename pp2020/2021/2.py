with open("text.txt", 'r') as f:
    x = list(map(lambda a: len(a.rstrip()), f.readlines()))
    print(*x)
for i in range(1, len(x)):
    if x[i] <= x[i-1]:
        print("NO")
        exit()
print("YES")