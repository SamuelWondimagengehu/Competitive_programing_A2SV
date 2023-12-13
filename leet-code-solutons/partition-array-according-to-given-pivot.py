class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []
        pivot_cnt = 0
        
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                pivot_cnt += 1
        
        return left + [pivot] * pivot_cnt + right
        
        