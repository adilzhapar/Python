def Average(x):
    sum = 0
    for i in x:
        sum += int(i)
    value = float(sum / len(x))
    return f'{value:.3f}'

n = int(input())
my_dict = {}
for i in range(n):
    name, gpa = input().split()
    if name not in my_dict:
        my_dict[name] = [gpa]
    else:
        my_dict[name] += [gpa]

for i in my_dict:
    my_dict[i] = Average(my_dict[i])

'''
ss=list(my_dict.items()) 
ss.sort(key = lambda x : x[1],  reverse=True )
print(*ss) 
'''
my_dict = dict(sorted(my_dict.items(), key = lambda x: x[1], reverse = True))
for x in my_dict:
    print("{}: {}".format(x, my_dict[x]))