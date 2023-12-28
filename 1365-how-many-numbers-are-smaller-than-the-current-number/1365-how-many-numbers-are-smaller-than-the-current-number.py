class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        book = defaultdict(int)
        
        for i in range(len(nums)):
            book[i] = 0
            
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if num > nums[j] and i != j:
                    book[i] += 1                    
                
        return book.values()