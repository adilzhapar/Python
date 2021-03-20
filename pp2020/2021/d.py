import re
emails = list(input().split())
nicks = []
domains = []
suffixes = []
for i in emails:
    x = re.search(r'(?P<nick>^.*)@', i)
    d = re.search(r'@(?P<dom>.*)\.', i)
    s = re.search(r'\.(?P<suf>.*$)', i)
    nicks.append(x.group('nick'))
    domains.append(d.group('dom'))
    suffixes.append(s.group('suf'))
print(*nicks)
print(*domains)
print(*suffixes)