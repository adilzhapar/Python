import re

handler = open("raw.data", 'r', encoding='utf8')
text = handler.read()

pattern = r"(?P<name>.*)\n{1}(?P<cnt>.*)x(?P<price>.*)\n{1}(?P<sum>.*)\n{1}Стоимость\n{1}(?P<total>.*)"
patric = re.compile(pattern)

for match in patric.finditer(text):
    print(match.group("name"), end=' => ')
    print(match.group("cnt"), end=' => ')
    print(match.group("price"), end=' => ')
    print(match.group("sum"), end=' => ')
    print(match.group("total"))

handler.close()
