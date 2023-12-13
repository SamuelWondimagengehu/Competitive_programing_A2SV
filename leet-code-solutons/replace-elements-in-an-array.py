class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        positions = {}
        
        for i, num in enumerate(nums):
            positions[num] = i
        
        for i, j in operations:
            index = positions[i]
            nums[index] = j
            positions[nums[index]] = index
        
        return nums
        