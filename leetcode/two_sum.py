class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = defaultdict(int)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in book:
                return [book[complement],i]
            else:
                book[nums[i]] = i
                
                # 3 : 0, 4 : 1, 2 : 2 
