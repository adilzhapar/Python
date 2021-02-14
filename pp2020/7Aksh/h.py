n = int(input())
group = list(map(str, input().split()))
m = int(input())
practice = list(map(str, input().split()))

print("Missed students:")
for student in group:
    if student not in practice:
        print("- {}".format(student))
print("Not in the group:")
for student in practice:
    if student not in group:
        print("- {}".format(student))
