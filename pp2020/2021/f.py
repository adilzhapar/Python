nums = list(map(int, input().split()))
uniq = {}
for i in nums:
    if i not in uniq:
        uniq[i] = 0
    else:
        uniq[i] += 1
if len(uniq.values()) == len(set(uniq.values())):
    print("Perfect")
else:
    print("Not perfect")