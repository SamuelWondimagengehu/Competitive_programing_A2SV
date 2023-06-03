class Solution:
    def cross_helper(self,nums, lo, mid, hi):
        left_sum , right_sum = -math.inf, -math.inf
        
        t_sum = 0
        for i in range(mid, lo - 1, -1):
            t_sum += nums[i]
            if t_sum > left_sum:
                left_sum = t_sum
        
        t_sum = 0
        for i in range(mid + 1, hi + 1):
            t_sum += nums[i]
            if t_sum > right_sum:
                right_sum = t_sum
        
        return right_sum + left_sum
    
    def find_max_subarray(self, nums, lo, hi):
        if hi == lo:
            return nums[lo]
        
        mid = (lo + hi) // 2
        
        left_sum = self.find_max_subarray(nums, lo, mid)
        right_sum = self.find_max_subarray(nums, mid + 1, hi)
        cross_sum = self.cross_helper(nums, lo, mid, hi)
            
        return max(cross_sum, max(left_sum, right_sum))
        
    def maxSubArray(self, nums: List[int]) -> int:
        ans = self.find_max_subarray(nums, 0, len(nums) - 1)
        return ans