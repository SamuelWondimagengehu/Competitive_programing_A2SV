def solution()->str:
    n = int(input())
    nums = input().split(" ")
    ex = [0] * 2

    for i, num in enumerate(nums):
        nums[i] = int(num)
    
    for num in nums:
        ex[num % 2] = 1

    if ex[0] and ex[1]:
        nums.sort()
    
    return " ".join([str(num) for num in nums])

print(solution())