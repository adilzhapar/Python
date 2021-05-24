s = input()
l = input()

def is_anagram(s, l):
    s = list(s)
    l = list(l)
    s.sort()
    l.sort()
    return s == l


print("YES" if is_anagram(s, l) else "NO")