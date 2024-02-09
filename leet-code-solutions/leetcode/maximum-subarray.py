class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lm = nums[0]
        gm = nums[0]

        for i in range(1, len(nums)):
            lm = max(nums[i], nums[i] + lm)
            if lm > gm:
                gm = lm
        
        return gm