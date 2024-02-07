class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        
        print(self.nums)    
    def sumRange(self, left: int, right: int) -> int:    
        sum_ = 0
        
        while left <= right:
            sum_ += self.nums[left]
            left += 1
        
        return sum_

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)