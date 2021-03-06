from collections import deque
cleans = deque()
n = int(input())
clean = dirty = 0
plates = list(map(int, input().split()))
for plate in plates:
    if len(cleans) == 0 and plate == 0:
        cleans.append(plate)
    elif len(cleans) == 0 and plate == 1:
        dirty += 1
    elif cleans[-1] == 0 and plate == 0:
        cleans.append(plate)
    elif cleans[-1] == 0 and plate == 1:
        dirty += 2
        cleans.pop()
print("Clean:{}\nDirty:{}".format(len(cleans), dirty))



