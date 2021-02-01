odd = list(map(int, input().split()))
odd.sort()

for i in odd:
    if i % 2 == 1:
        print(i)
        exit()

print(0)
