class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freqs = [nums[i] for i in range(0, len(nums), 2)]
        vals = [nums[i + 1] for i in range(0, len(nums), 2)]
        
        ans = []
        
        for freq, val in zip(freqs, vals):
            for i in range(freq):
                ans.append(val)
                
        return ans