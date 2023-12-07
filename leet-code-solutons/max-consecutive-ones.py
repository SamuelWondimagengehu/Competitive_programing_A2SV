class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        book = defaultdict(int)
        for i, num in enumerate(nums):
            if i == 0 and num == 1:
                book[i] = 1
            else:
                if book[i - 1] and num:
                    book[i] = book[i - 1] + 1
                elif not book[i - 1] and num:
                    book[i] = 1
                else:
                    book[i] = 0
        
        counts = sorted(list(book.values()))
        return counts[-1]
        

            
        