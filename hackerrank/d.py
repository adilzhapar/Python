import re

m = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*([aeiouAEIOU]{2,})+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+', input().strip())

if len(m) != 0:
    print(*m, sep='\n')
else:
    print(-1)