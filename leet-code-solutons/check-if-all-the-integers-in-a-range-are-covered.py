class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        store = set()
        
        for l_i, r_i in ranges:
            for i in range(l_i, r_i + 1):
                store.add(i)
        
        for i in range(left, right + 1):
            if i not in store:
                return False
        
        return True