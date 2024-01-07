class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = curr = sum(nums[:k])
        n = len(nums)
        
        for i in range(k, n):
            curr += nums[i] - nums[i - k]
            window = max(curr, window)
        
        return window / k