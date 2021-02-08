import re

txt = input()
word = input()
x = re.search(word, txt)
if x:
    print("First time {} occurred in position:".format(word), x.start())
else:
    print("Not found")


