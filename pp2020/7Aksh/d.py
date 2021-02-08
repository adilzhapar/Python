s = input()
x = list(map(int, input().split()))

a, b = 0, 0
xy = []

for i in s:
    if i == "R":
        b += 1
        xy.append([b, a])
    elif i == "L":
        b -= 1
        xy.append([b, a])
    elif i == "U":
        a += 1
        xy.append([b, a])
    else:
        a -= 1
        xy.append([b, a])


if x in xy:
    print("Passed")
else:
    print("Missed")



