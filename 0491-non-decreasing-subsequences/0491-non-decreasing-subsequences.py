class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subsequences = []
        
        def dfs(i, prev):
            if i == len(nums):
                if len(subsequences) >= 2:
                    res.add(tuple(subsequences))
                return
            
            dfs(i + 1, prev)
            
            if nums[i] >= prev:
                subsequences.append(nums[i])
                dfs(i + 1, nums[i])
                subsequences.pop()
                
        dfs(0, -inf)
        return list(res)