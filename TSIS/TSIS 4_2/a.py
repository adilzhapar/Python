import re
n = int(input())
for i in range(n):
    s = input()
    x = re.search(r"^([+]|[-]|[.]|[+.]|[-.]|\d*[.])[0-9]*.*[0-9]+", s)
    try:
        y = float(x.group(0))
        if x:
            print(True)
        else:
            print(False)
    except:
        print(False)
    