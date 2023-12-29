class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        c1, c2 = Counter(nums1), Counter(nums2)
        
        dups = set()
        
        for num in nums1:
            if num in nums2:
                dups.add(num)
            
        for k, v in c1.items():
            if c1[k] > c2[k]:
                count = c2[k]
                while count:
                    answer.append(k)
                    count -= 1
            elif c1[k] < c2[k]:
                count = c1[k]
                while count:
                    answer.append(k)
                    count -= 1
            else:
                count = c1[k]
                while count:
                    answer.append(k)
                    count -= 1
                    
        return answer