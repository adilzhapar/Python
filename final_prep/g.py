n = int(input())
time = []
# Bubble sort
for i in range(n):
    t = list(map(int, input().split()))
    time.append(t)
for i in range(0, len(time)-1):
    for j in range(0, len(time)-i-1):
        if time[j][0] > time[j+1][0]:
            time[j], time[j+1] = time[j+1], time[j]
        elif time[j][0] == time[j+1][0]:
            if time[j][1] > time[j + 1][1]:
                time[j], time[j + 1] = time[j + 1], time[j]
            if time[j][1] == time[j + 1][1]:
                if time[j][2] > time[j+1][2]:
                    time[j], time[j + 1] = time[j + 1], time[j]

print(*time)