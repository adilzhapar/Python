S = input()
k = input()
import re
pattern = re.compile(k)

for match in re.finditer(pattern, S):
    print("({0}, {1})".format(match.start(), match.end()-1))