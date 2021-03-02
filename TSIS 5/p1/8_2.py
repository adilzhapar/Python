# longest word
with open('input.txt', 'r') as txt:
    words = txt.read().split()
    max_len = len(max(words, key=len))
print(*[word for word in words if max_len==len(word)])