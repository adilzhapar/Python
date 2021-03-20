nums = list(input().split())
cnt = 0
for i in nums:
    if len(i) % 2 == 0:
        cnt += 1
print(cnt)

# import os
# for i in range(4):
#     handler = open(chr(ord("c")+i) + '.py', 'w')
