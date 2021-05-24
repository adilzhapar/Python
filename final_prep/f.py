n = int(input())
pills = list(map(int, input().split()))
q = int(input())
answers = []

def See(l, r, pills):
    cnt = 1
    max = pills[l]
    for i in range(l, r+1):
        if pills[i] > max:
            cnt += 1
            max = pills[i]
    return cnt

for i in range(q):
    l, r = map(int, input().split())
    answers.append(See(l, r, pills))
print(*answers)
