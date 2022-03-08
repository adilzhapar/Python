import re

with open('newproxy.txt', 'r') as f:
    x = f.read()


pattern = r'(?P<IP>.*):(?P<host>.*)@(?P<user>.*):(?P<pass>.*)\n{1}'
patric = re.compile(pattern)

for item in patric.finditer(x):
    print(item.group('IP'), end=" => ")
    print(item.group('host'), end=" => ")
    print(item.group('user'), end=" => ")
    print(item.group('pass'))