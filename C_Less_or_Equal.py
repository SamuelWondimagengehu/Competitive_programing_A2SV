def solution():
    n, k = input().split(" ")
    n, k = int(n), int(k)
    nums = input().split(" ")

    for i, num in enumerate(nums):
        nums[i] = int(num)

    nums.sort()
    if k > 0:
        nums_slice = nums[:k]
        x = nums_slice[k - 1] + 1
    else:
        x = nums[k] - 1
    count = 0
    for num in nums:
        if x >= num:
            count += 1
        
    if count != k or x <= 1:
        x = -1

    return x
    
print(solution())
