import sys

def myAtoi(s):
    s = s.strip()

    minus = False
    if s[0] == '-':
        minus = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    s = ''.join(list(filter(lambda x: x in "0123456789", s)))
    while(s[0] == '0'):
        s = s[1:]
    if minus == True:
        if int(s) > 2**31 - 1:
            return -2**31
        else: return int(s) * (-1)
    else:
        if int(s) > 2**31 - 1:
            return 2**31 - 1
        else:
            return int(s)


print(myAtoi("words and 987"))