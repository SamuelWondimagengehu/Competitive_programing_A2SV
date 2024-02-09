class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        total = 0

        frequency = {0: 1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            target_sum = prefix_sum - k

            if target_sum in frequency:
                total += frequency[target_sum]
            
            frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1
        
        return total