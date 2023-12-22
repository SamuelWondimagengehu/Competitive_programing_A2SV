class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_1 = sum(nums)
        book = defaultdict(list)
        count_0, max_division = 0, count_1
        book[count_1].append(0)
        
        for i, num in enumerate(nums):
            count_0 += int(num == 0)
            count_1 -= int(num == 1)

            book[count_0 + count_1].append(i + 1)
            max_division = max(max_division, count_1 + count_0)

        return book[max_division]