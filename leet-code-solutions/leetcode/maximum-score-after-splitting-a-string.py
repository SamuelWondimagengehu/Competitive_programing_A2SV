class Solution:
    def maxScore(self, s: str) -> int:
        nums = list(map(int, list(s)))
        right = sum(nums)
        left = 0
        
        max_score = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                left += 1
            else:
                right -= 1

            max_score = max(max_score, left + right)
        
        return max_score
