pair = list(map(int,input().split()))

for i in range(0, len(pair)-1):
    if pair[i] > 0 and pair[i+1] > 0:
        print(pair[i], pair[i+1])
        break
    elif pair[i] < 0 and pair[i+1] < 0:
        print(pair[i], pair[i+1])
        break
    else:
        continue
 