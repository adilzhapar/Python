l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
last = l1 + l2
last.sort()

if len(last) % 2 == 0:
    med = float((last[len(last) // 2] + last[len(last) // 2 - 1]) / 2)
else:
    med = float(last[len(last) // 2])
print(med)