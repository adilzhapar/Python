n = int(input())

gpa = {}
for i in range(n):
    s, x = input().split()
    if s not in gpa:
        gpa[s] = []
    gpa[s].append(int(x))

for i in gpa:
    x = sum(gpa[i]) / len(gpa[i])
    gpa[i] = f'{x:.3f}'

gpa = dict(sorted(gpa.items(), key=lambda x: x[0]))

for i, j in gpa.items():
    print('{}: {}'.format(i, j))

