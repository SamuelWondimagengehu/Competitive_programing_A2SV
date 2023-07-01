class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker, placeholder = 0, 0
        
        while seeker <= len(nums) - 1:
            if nums[seeker] != 0:
                nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                placeholder += 1
            seeker += 1
            