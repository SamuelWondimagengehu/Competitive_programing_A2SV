class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [val for val in nums if val * -1 <= 0]
        negatives = [val for val in nums if val * -1 > 0]
        
        ans = []
        for pos, neg in zip(positives, negatives):
            ans.append(pos)
            ans.append(neg)

        return ans