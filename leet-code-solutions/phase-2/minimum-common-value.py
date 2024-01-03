class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = 0, 0
        
        while (a < len(nums1) and b < len(nums2)) and nums1[a] != nums2[b]:
            if nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        
        
        if a == len(nums1) or b == len(nums2):
            return -1
        else:
            return nums1[a]
        