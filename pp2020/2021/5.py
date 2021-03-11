word = input()
k = input()

points = []
positions = []
last = []

for i in range(len(word)):
    positions.append(i)
    if word[i] == k:
        points.append(i)
MIN = 100
for i in positions:
    for j in points:
        x = abs(i-j)
        if x < MIN:
            MIN = x
    last.append(MIN)
    MIN = 100
print(*last)

    
