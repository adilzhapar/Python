import re

s = input()
nums = re.split("[,]|[.]", s)
print(*nums, sep='\n')