class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        answer = 0
        for k,v in counts.items():
            answer += (v * (v - 1)) // 2
        return answer