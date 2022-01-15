s = 'IVI'
sum = 0
for i in range(len(s)):
    if s[i] == 'I':
        if i != len(s) - 1:
            if s[i+1] == 'V':
                sum += 4
            elif s[i+1] == 'X':
                sum += 9
            else: sum += 1
        else: sum += 1  
print(sum)