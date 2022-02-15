def compress(chars):
    s = ""
    for i in chars:
        if i not in s:
            x = chars.count(i)
            t = i + str(x)
            s += t
            t = ""
    chars.clear()
    return list(s)
        
print(compress(["a","a","b","b","c","c","c"]))
