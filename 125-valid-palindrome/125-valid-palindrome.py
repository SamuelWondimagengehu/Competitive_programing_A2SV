import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()        
        
        s = re.sub(r'[^a-zA-Z0-9]', '',s)
        
        a_ptr, b_ptr = 0, len(s) - 1
        
        while a_ptr <= b_ptr:
            if s[a_ptr] != s[b_ptr]:
                return False
            a_ptr += 1
            b_ptr -= 1
        
        return True
                