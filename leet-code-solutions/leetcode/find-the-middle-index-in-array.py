class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right, left = sum(nums), 0

        for i, num in enumerate(nums):
            right -= num #take off the current number
            
            if right == left:
                return i
            
            left += num #add the current number to the left side sum

        return -1


        
        