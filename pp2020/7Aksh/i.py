n = int(input())
nums = list(map(lambda x: str(x), list(map(int, input().split()))))
k = int(input())
a = nums[0:k]
b = nums[k:n]

x = "".join(a)
y = "".join(b)
print(int(x)*int(y))
print(x)
print(y)