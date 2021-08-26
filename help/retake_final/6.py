students = list(map(str, input().split()))
cnt = 0
for i in range(len(students)):
    for j in range(len(students)):
        if students[i] == students[j] and i < j:
            cnt += 1
print(cnt)