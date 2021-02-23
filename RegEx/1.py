import re

txt = "number of great BMW cars 530"

x = re.search(r"(?P<mark>[A-Z]+).*(?P<number>\b[0-9]+)", txt)


print(x.group("mark"))
print(x.group('number'))

# y = re.search(r".*(?P<mark>\b[A-Z]+)", txt)
# print(y.group("mark"))