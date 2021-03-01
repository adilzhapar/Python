n = int(input())
my_list = list(map(set, input().split()))
z = my_list[0]
for i in my_list:
    z.intersection_update(i)
if z:
    print(*z)
else:
    print("NO COMMON CHARACTERS")
