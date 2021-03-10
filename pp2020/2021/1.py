import re
date = input()
#1299.01.01-1922.12.31
txt = re.search(r"(?P<year>1299|1[3-8]\d{2}|19[0-1][0-9]|192[0-2])[.](?P<month>0[1-9]|1[0-2])[.](?P<day>0[1-9]|[1-2][0-9]|3[0-1])", date)
# x = re.search(r"(?P<day>0[1-9]|[1-2][0-9]|3[0-1])", date)


if txt:
    print("yes")
else:
    print("no")
