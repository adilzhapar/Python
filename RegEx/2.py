import re

file  = open("raw.data", "r", encoding='utf8')
txt = file.read()

BINpat = r"\nБИН.*(?P<BIN>\b[0-9]+)"

x = re.search(BINpat, txt).group("BIN")
print(x)
file.close()