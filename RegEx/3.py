import re

file = open("raw.data", 'r', encoding='utf8')
txt = file.read()

patric = r"\nБИН.*(?P<BIN>\b[0-9]+).*\nНДС.*(?P<NDS>\b[0-9]+)"
x = re.compile(patric)

for match in x.finditer(txt):
    print(match.group('BIN'))
    print(match.group('NDS'))