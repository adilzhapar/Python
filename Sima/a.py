# [1, 2, 3]
# [0, 1, 0]
# [0, 1, 0, 0, 2, 0, 0, 3, 0]



a = [1, 2, 3]
b = [0, 1, 0]

print("Original 1-d arrays:")
print(a)
print(b)

result = []
print("Kronecker product of the said arrays:")
for i in a:
    for j in b:
        result.append(i*j)
print(result)


print("Original Higher dimension:")

aa = []
cnt = 0

for i in range(3):
    ll = []
    for j in range(3):
        ll.append(cnt)
        cnt += 1
    aa.append(ll)

print(aa)

bb = []
cnt2 = 3

for i in range(3):
    ll = []
    for j in range(3):
        ll.append(cnt2)
        cnt2 += 1
    bb.append(ll)

print(bb)

res2 = []
for arr in aa:
    for i in bb:
        ll = []
        for elem in arr:
            for j in i:
                ll.append(elem*j)
        res2.append(ll)


print("Kronecker product  of the said arrays:")
for i in res2:
    print(i)
    