handler = open("input.txt", 'r')
text = handler.read().split()
new_txt = list(map(str, input().split()))
text += new_txt
print(*text)