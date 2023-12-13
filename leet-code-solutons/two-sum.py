class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in book:
                return [book[comp], i]
            else:
                book[num] = i
                
       
    