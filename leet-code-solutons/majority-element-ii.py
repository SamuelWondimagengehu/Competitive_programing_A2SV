class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        book = Counter(nums)
        
        ans = [k for k, val in book.items() if val > len(nums) // 3]
        
        return ans
        