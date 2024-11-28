class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(filter(lambda x: len(x) > 0, s.split(" ")))
    
        return len(l.pop())