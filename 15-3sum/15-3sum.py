class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # -4 -1 -1 0 1 2
        ans = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            a_ptr, b_ptr = i + 1, len(nums) - 1
            
            while a_ptr < b_ptr:
                threeSum = nums[a_ptr] + nums[b_ptr] + num
                
                if threeSum > 0:
                    b_ptr -= 1
                elif threeSum < 0:
                    a_ptr += 1
                else:
                    ans.append([num, nums[a_ptr], nums[b_ptr]])
                    a_ptr += 1
                    while nums[a_ptr] == nums[a_ptr - 1] and a_ptr < b_ptr:
                        a_ptr += 1
        return ans
                
            
            