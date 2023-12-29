class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        a_ptr, b_ptr = 0, 0
        answer = []
        
        while a_ptr < len(nums1) and b_ptr < len(nums2):
            if nums1[a_ptr] < nums2[b_ptr]:
                a_ptr += 1
            elif nums1[a_ptr] > nums2[b_ptr]:
                b_ptr += 1
            else:
                answer.append(nums1[a_ptr])
                a_ptr += 1
                b_ptr += 1
                
        return answer