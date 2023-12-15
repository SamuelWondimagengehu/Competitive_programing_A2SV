class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num_freq = Counter(arr)
        freq_num = Counter()
        
        for num, freq in num_freq.items():
            freq_num[freq] = num
        
        ans = [count for val, count in freq_num.items() if val > len(arr) // 4]
        
        return ans[0]
        