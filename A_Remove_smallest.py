def solution():
  s = int(input()) - 1
  nums = input().split(" ")

  for i, num in enumerate(nums):
    nums[i] = int(num)

  nums.sort()
  ok = True
  for i, num in enumerate(nums):
    if i < s:
      ok &= (nums[i + 1] - num <= 1)
    if ok == False:
      return "NO"
  return "YES"

test_cases = int(input())
for _ in range(test_cases):
  print(solution())
