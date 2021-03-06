from collections import deque
cleans = deque()
n = int(input())
plates = list(map(int, input().split()))
for i in plates:
    if i == 0:
        cleans.append(1)
    else:
        if len(cleans) != 0:
            cleans.pop()
print("Clean:{}\nDirty:{}".format(len(cleans), n - len(cleans)))
