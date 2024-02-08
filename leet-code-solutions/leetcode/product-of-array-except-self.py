class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = suffix = 1
        pref = [0] * n
        suff = [0] * n

        for i in range(n):
            pref[i] = prefix
            prefix *= nums[i]
        
        for i in range(n - 1, -1, -1):
            suff[i] = suffix
            suffix *= nums[i]
      
        answer = [suff[i] * pref[i] for i in range(n)]

        return answer
        
            