class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3
        nums = [x - 1, x, x + 1]

        if sum(nums) == num:
            return nums
        else:
            return []