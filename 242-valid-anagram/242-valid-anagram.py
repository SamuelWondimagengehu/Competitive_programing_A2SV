class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if Counter(s) == Counter(t): # a:3,n:1,g:1,r:1,m:1
            return True
        else:
            return False
        