import re

def email(s):
    x = re.search(r'^[a-z]+[@][a-z]+[.][a-z]+', s)
    if x:
        print("yes")
    else:
        print("no")

s = input()
email(s)