# mail reader
import re
arr = list(map(str, input().split()))
logs = []
mails = []
domains = []
for i in arr:
    logs.append(re.search(r'(^\w+)', i).group(0))
    mails.append(re.search(r'@(?P<mail>[a-z0-9]+)', i).group('mail'))
    domains.append(re.search(r'[.](?P<dom>[a-z]{2,4}$)', i).group('dom'))

print('nicknames:\n', *sorted(logs))
print('domain name:\n', *sorted(mails))
print('suffix:\n', *sorted(domains))
