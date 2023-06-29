class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        positions = {}
        
        for i in range(len(nums)):
            positions[nums[i]] = i
        
        for i, j in operations:
            index = positions[i]
            nums[index] = j
            positions[nums[index]] = index
                
        return nums