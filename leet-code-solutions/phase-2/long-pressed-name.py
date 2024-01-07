class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m = len(name), len(typed)
        
        if m < n:
            return False
        
        if name[0] != typed[0]:
            return False
        
        i, j = 0, 0
        
        while i < n:
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if name[i - 1] == typed[j]:
                    j += 1
                else:
                    return False
        
            if j == m and i < n:
                return False
        
        if j < m:
            while j < m:
                if name[i - 1] != typed[j]:
                    return False
                j += 1
        
        return True
                
            
            