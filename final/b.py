s = input()
arr = input().split()

def is_anagram(s, l):
    s = list(s)
    l = list(l)
    s.sort()
    l.sort()
    return s == l

test = False
last = []
for i in arr:
    if not is_anagram(s, i):
        last.append(i)
last.sort()
print(*last)
