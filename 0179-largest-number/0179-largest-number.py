class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0 or nums == None:
            return ""
        
        nums = list(map(str, nums))
        
        n = len(nums)
        
        for i in range(n):
            for j in range(n - 1):
                first, second = nums[j + 1] + nums[j], nums[j] + nums[j + 1]
                if first > second:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        if nums[0][0] == "0":
            return "0"
        else:
            return "".join(nums)