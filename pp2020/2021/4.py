nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j] and i != j:
            print(nums[i], nums[j])