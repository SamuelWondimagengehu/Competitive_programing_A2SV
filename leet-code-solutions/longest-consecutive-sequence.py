class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            length = 0
            if (num - 1) not in num_set:
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest
        