handler = open('a.txt', 'r')
arr = handler.read().split()
handler.close()

print(arr)
