class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        
        for i in range(length):
            if i not in nums:
                return i
            
        return length
        