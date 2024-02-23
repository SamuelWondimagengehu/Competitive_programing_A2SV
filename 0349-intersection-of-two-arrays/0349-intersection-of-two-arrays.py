class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
                
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.add(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                ans.add(nums2[i])
        
        return list(ans)