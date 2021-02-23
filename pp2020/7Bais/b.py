import re
s = input()
x = re.search(r"^\w*$", s)
if x:
    print("Founded")
else:
    print("No")