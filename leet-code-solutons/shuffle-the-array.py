class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half, second_half = nums[0:n], nums[n:len(nums)]
        
        ans = []
        
        for first, second in zip(first_half, second_half):
            ans.append(first)
            ans.append(second)
        
        return ans
        