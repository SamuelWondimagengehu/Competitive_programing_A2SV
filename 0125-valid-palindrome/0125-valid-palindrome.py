class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        vals = list(s)
        string = ""
        
        for val in vals:
            if val.isalnum():
                string += val
        
        a_ptr, b_ptr = 0, len(string) - 1
        
        while a_ptr <= b_ptr:
            if string[a_ptr] != string[b_ptr]:
                return False
            a_ptr += 1
            b_ptr -= 1
            
        return True
        