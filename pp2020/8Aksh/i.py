s = input()
t = input()

s = list(s)
t = list(s)
s.sort()
t.sort()

if s == t:
    print("Anagram")
else:
    print("Not anagram")