class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x)
        a, b = 0, len(c)-1
        
        while a <= b:
            if c[a]!=c[b]:
                return False
            else:
                a = a+1
                b = b-1
        return True