nums = list(map(int, input().split()))
n = len(nums)
for i in range(n//2):
    nums[i], nums[-i-1] = nums[-i-1], nums[i]
for i in nums:
    print(i, end=' ')

